import json
from re import sub


from django.http      import JsonResponse, HttpResponse
from django.views     import View
from django.db.models import Q

from user.utils    import login_decorator
from Email.models  import Category, Email, UserCategory, UserEmail
from user.models   import User

# 메일 구독, 취소 API
class SubscribeView(View):
    @login_decorator
    def post(self, request):
        try:
            data      = json.loads(request.body)
            user      = request.user
            category  = data['category']
            
            print(user, category)
            
            # if not User.objects.filter(name=user):
            #     return JsonResponse({'message' : 'INVALID_USER'}, status=400)
            
            if not Category.objects.filter(name=category).filter().exists():
                return JsonResponse({'message' : 'INVALID_CATEGORY'}, status=400)
            
            print('11111111111111111111111111111111111')
            user      = User.objects.get(name=user).id
            category  = Category.objects.get(name=category).id

            print('22222222222222222222222')
            if UserCategory.objects.filter(user_id=user, category_id=category).exists():
                UserCategory.objects.get(user_id=user, category_id=category).delete()
                return JsonResponse({'message' : 'SUCCESS'}, status=201)
    
            UserCategory.objects.create(
                user_id      = user,
                category_id  = category
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
        
    # 구독자 조회 API
    def get(self, request):
        category_list = request.GET.get('category', None)
        q = Q()
        
        if category_list:
            for category in category_list:
                Q.add(Q(category=category), q.AND)
        
        subscribes = UserCategory.objects.filter(q)
        
        subscribe_list = [{
            'category' : subscribe.category.name,
            'subscriber' : subscribe.user.name
        } for subscribe in subscribes]
        
        return JsonResponse({'message' : 'SUCCESS', 'subscribe_list' : subscribe_list}, status=200)
    
# 구독 중인 모든 유저 에게 메일을 전송하는 API
class SendingMailView(View):
    def post(self, request):
        try:
            data    = json.loads(request.body)
            subject = data['subject']
            content = data['content']
            users   = User.objects.all()
            
            mail = [{
                'mailto' : user.name,
                'subject' : subject,
                'content' : content
            } for user in users]
            
            Email.objects.create(
                subject = subject,
                content = content
            )
            
            for user in users:
                if not User.objects.filter(name=user.name).exists():
                    return JsonResponse({'message' : 'INVALID_USER'}, status=400)
                user  = User.objects.get(name=user.name).id
                email = Email.objects.get(subject=subject).id
                
                user.email.add(user)
                
            return JsonResponse({'status' : 'success', 'mail_list' : mail }, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
    
    def delete(self, request):
        pass

class SearchEmaillistView(View):
    def get(self, request):
        pass
            