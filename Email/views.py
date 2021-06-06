import json
import datetime

from django.http       import JsonResponse
from django.views      import View
from django.db.models  import Q

from user.utils    import login_decorator
from Email.models  import Category, Email, UserCategory, UserEmail
from user.models   import User

# 메일 구독, 취소 API
class SubscribeView(View):
    @login_decorator
    def post(self, request):
        try:
            user_id     = request.user.id
            data        = request.POST
            categories = data.getlist('category')
            print(categories)
            
            for category in categories: 
                print(category)  
                if not Category.objects.filter(name=category).filter().exists():
                    return JsonResponse({'message' : 'INVALID_CATEGORY'}, status=400)
                
                category  = Category.objects.get(name=category).id
        
                UserCategory.objects.create(
                    user_id      = user_id,
                    category_id  = category
                )
                
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
        
    # 구독 취소 API
    @login_decorator
    def delete(self, request):
        try:
            user_id     = request.user.id
            data        = request.POST
            categories = data.getlist('category')
            
            for category in categories:  
                if not Category.objects.filter(name=category).filter().exists():
                    return JsonResponse({'message' : 'INVALID_CATEGORY'}, status=400)
                
                category  = Category.objects.get(name=category).id

                if UserCategory.objects.filter(user_id=user_id, category_id=category).exists():
                    UserCategory.objects.get(user_id=user_id, category_id=category).delete()
                    
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
    
    # 구독자 조회 API
    def get(self, request):
        category_list = request.GET.getlist('category', None)
        q = Q()
        
        if category_list:    
            for category in category_list:
                q.add(Q(category__name=category), q.OR)
        subscribes = UserCategory.objects.filter(q)
        
        subscribe_list = [{
            'category'   : subscribe.category.name,
            'subscriber' : subscribe.user.name
        } for subscribe in subscribes]
        
        return JsonResponse({'message' : 'SUCCESS', 'subscribe_list' : subscribe_list}, status=200)
    
# 구독 중인 모든 유저 에게 메일을 전송하는 API
class SendingMailView(View):
    @login_decorator
    def post(self, request):
        try:
            sender_id  = request.user.id
            data       = request.POST
            category   = data['category']
            subject    = data['subject']
            content    = data['content']
            users      = User.objects.all()
            mail = [{
                'mailto' : user.name,
                'subject' : subject,
                'content' : content
            } for user in users]
            
            sender = User.objects.filter(id=sender_id).first()
            email=Email.objects.create(
                subject = subject,
                content = content,
                sender  = sender
            )
            
            category_id = Category.objects.get(name=category).id
            
            subscribers = UserCategory.objects.filter(category_id=category_id)
            for subscriber in subscribers:
                receiver  = subscriber.user_id
                email_id = email.id
                UserEmail.objects.create(
                    user_id = receiver,
                    email_id = email_id
                )
                
            return JsonResponse({'status' : 'success', 'mail_list' : mail }, status=200)
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
            # for receiver in email]
        
        print(email_list)   
        return JsonResponse({'message' : 'success', 'email_list' : email_list}, status=200)
        
    @login_decorator
    def delete(self, request):
        try:
            user = request.user
            data = json.loads(request.body)
            delete_subject = data['subject']
            
            if not Email.objects.filter(subject=delete_subject).exists():
                return JsonResponse({'message' : 'INVALID_SUBJECT'}, stauts=400)
            deleted_id = Email.objects.get(subject=delete_subject).id
            Email.objects.get(subject=delete_subject).delete()
            Email.objects.filter(id=deleted_id).update(deleted_at=datetime.date.today())
            
            return JsonResponse({'message' : 'success'} , status=201)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
        
# 메일 발송 이력조회
class CheckShippingHistoryView(View):
    def get(self, request):
        subject_list = request.GET.getlist('subject',None)
        q = Q()
        
        if subject_list:    
            for subject in subject_list:
                q.add(Q(subject=subject), q.OR)

        emails = Email.objects.filter(q)
        
        data = [{
            'id' : email.id,
            'subject' : email.subject,
            'content' : email.content,
            'subcriber': {
                'id' : receiver.id,
                'name' : receiver.name,
                'subscribe_categories' : [category.category.name for category in UserCategory.objects.filter(user_id=receiver.id)]
            } 
            }for email in emails for receiver in email.receiver.all()]
        
        return JsonResponse({'message' : 'success', 'data' : data}, status=200)