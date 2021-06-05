import json
import requests
import re
import bcrypt
import jwt

from django.http    import JsonResponse, HttpResponse
from django.views   import View

from subscribe_email.my_settings    import SECRET_KEY, ALGORITHM
from user.models    import User

class SignupView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            print(data)
            name     = data['name']
            email    = data['email']
            password = data['password']
            print('111111111111111111111111111')
            password_regex = re.compile("(?=.*\d)(?=.*[a-z]).{8,32}$", re.IGNORECASE)
            if not password_regex.match(password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)
            
            # # email_regex = re.compile("^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$")
            # if  User.objects.filter(email=email).exists():
            #     return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)
            
            if not name:
                return JsonResponse({'message' : 'INVALID_NAME'}, status=400)
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'DUPLICATED_EMAIL'}, status=400)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(
                email = email,
                password = hashed_password,
                name = name
            )
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, statu=400)
        
class SigninView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data['email']
            password = data['password']
            
            if not User.objects.get(email=email):
                return JsonResponse({'message' : 'INVALID_USER'}, status=401)
            
            user = User.objects.get(email=email)
            hashed_password = user.password
            print(hashed_password)
            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=401)
            token = jwt.encode({'user_id': user.id}, SECRET_KEY, algorithm=ALGORITHM)
            print(token)
            return JsonResponse({'message': 'SUCCESS', 'access_token': token.decode('utf-8')}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        