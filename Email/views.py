import json


from django.http   import JsonResponse, HttpResponse
from django.views  import View

from user.utils import login_decorator
from Email.models  import Category, Email, UserCategory, UserEmail
from user.models import User

# 메일 구독, 취소 API
class SubscribeView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            category = data['category']
            user = User.objects.get(email=email).id
            category = Category.objects.get(name=category).id
        
            if UserCategory.objects.filter(user_id=user, category_id=category).exists():
                UserCategory.objects.get(user_id=user, category_id=category).delete()
                return JsonResponse({'message' : 'SUCCESS'}, status=201)
    
            UserCategory.objects.create(
                user_id = user,
                category_id = category
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)