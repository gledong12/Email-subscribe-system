import json

from django.http  import JsonResponse, HttpResponse
from django.views import View
from Email.models import category, Email, UserCategory, UserEmail