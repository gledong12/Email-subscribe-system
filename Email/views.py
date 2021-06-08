import json
import datetime

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from user.utils    import login_decorator
from Email.models  import Category, Email, UserCategory, UserEmail
from user.models   import User

# 메일 구독
class SubscribeView(View):
    @login_decorator
    def post(self, request):
        try:
            user_id     = request.user.id
            data        = request.POST
            categories  = data.getlist('category')
           
            for category in categories: 
                if not Category.objects.filter(name=category).filter().exists():
                    return JsonResponse({'message' : 'INVALID_CATEGORY'}, status=400)
                
                category  = Category.objects.get(name=category).id
                
                if UserCategory.objects.filter(user_id=user_id, category_id=category).exists():
                    return JsonResponse({'message' : 'ALREADY_SUBSCRIBE'}, status=400)
        
                UserCategory.objects.create(
                    user_id      = user_id,
                    category_id  = category
                )
                
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
    
    @login_decorator
    def get(self, request):
        category_list = request.GET.getlist('category', None)
        q = Q()
        
        if not category_list:
            for category in category_list:
                q.add(Q(category__name=category), q.OR)
        
        subscribes = UserCategory.objects.filter(q)
        
        subscribe_list = [{
            'category'   : subscribe.category.name,
            'subscriber' : subscribe.user.name
        } for subscribe in subscribes]
        
        return JsonResponse({'message' : 'SUCCESS', 'subscribe_list' : subscribe_list}, status=200)
          
# 구독 취소 API
class UnSubscribeView(View): 
    @login_decorator
    def post(self, request):
        try:
            user_id     = request.user.id
            data        = request.POST
            categories  = data.getlist('category')
            
            for category in categories:  
                if not Category.objects.filter(name=category).filter().exists():
                    return JsonResponse({'message' : 'INVALID_CATEGORY'}, status=400)
                
                category  = Category.objects.get(name=category).id

                if not UserCategory.objects.filter(user_id=user_id, category_id=category).exists():
                    return JsonResponse({'message' : 'DO_NOT_EXIST_IN_SUBSCRIBE_LIST'})
                UserCategory.objects.get(user_id=user_id, category_id=category).delete()        
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
 
# 구독 중인 모든 유저 에게 메일을 전송하는 API
class SendingMailView(View):
    @login_decorator
    def post(self, request):
        try:
            sender_id  = request.user.id
            data       = request.POST
            category_list  = data.getlist('category')     
            subject    = data['subject']
            content    = data['content']
            q = Q()
            
            if not category_list:
                return JsonResponse({'message': 'DO_NOT_EXIST'}, status=400)
            else:
                for category in category_list:
                    q.add(Q(category__name=category), q.OR)
            
            subscribers = UserCategory.objects.filter(q).prefetch_related('user')

            mail = [{
                'mailto' : subscriber.user.name,
                'subject' : subject,
                'content' : content
            } for subscriber in subscribers]
            
            sender = User.objects.filter(id=sender_id).first()
            
            email=Email.objects.create(
                subject = subject,
                content = content,
                sender  = sender
            )
            
            for subscriber in subscribers:
                receiver  = subscriber.user_id
                email_id = email.id
                UserEmail.objects.create(
                    user_id = receiver,
                    email_id = email_id
                )

            return JsonResponse({'message': 'success', 'mail_list' : mail}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)

# 이메일 발송리스트 조회
class GetSendingListView(View):   
    @login_decorator
    def get(self,request, email_id):
        emails = UserEmail.objects.filter(email_id=email_id)
        email_list=[
            {
                'ID'         : email.email.id,
                'Created_at' : email.email.created_at,
                'Updated_at' : email.email.updated_at,
                'Deleted_at' : email.email.deleted_at,
                'Sender'     : email.email.sender.name,
                'Receiver'   : email.user.name,
                'Subject'    : email.email.subject,
                'Content'    : email.email.content}
            for email in emails]
        
        return JsonResponse({'message' : 'success', 'email_list' : email_list}, status=200)
    
class DelteEmailView(View):    
    @login_decorator
    def post(self, request):
        try:
            data            = request.POST
            delete_email_id = data['email_id']

            if not Email.objects.filter(id=delete_email_id).exists():
                return JsonResponse({'message' : 'INVALID_SUBJECT'}, status=400)

            Email.objects.filter(id=delete_email_id).update(deleted_at=datetime.date.today())
            return JsonResponse({'message' : 'success'}, status=201)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
        
class CheckShippingHistoryView(View):
    @login_decorator
    def get(self, request):
        subject_list = request.GET.getlist('subject',None)
        q = Q()
        
        if subject_list:    
            for subject in subject_list:
                if not Email.objects.filter(subject=subject).exists():
                    return JsonResponse({'message' : 'INVALID_SUBJECT'}, status=400)
                q.add(Q(subject=subject), q.OR)
            
        emails = Email.objects.filter(q)
        
        data = [{
            'id'       : email.id,
            'subject'  : email.subject,
            'content'  : email.content,
            'subcriber': {
                'id'     : receiver.id,
                'email'  : receiver.email,
                'name'   : receiver.name,
                'subscribe_categories' : [category.category.name for category in UserCategory.objects.filter(user_id=receiver.id)]
            } 
            }for email in emails for receiver in email.receiver.all()]
        
        return JsonResponse({'message' : 'success', 'data' : data}, status=200)
