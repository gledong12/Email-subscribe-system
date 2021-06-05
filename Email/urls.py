from django.urls import path
from .views import SubscribeView, SendingMailView, SearchEmaillistView

urlpatterns = [
    path('subscirbe', SubscribeView.as_view()),
    path('mail', SendingMailView.as_view()),
    path('inbox/<str:email_name>')
]
