from django.urls import path
from .views import (SubscribeView, 
                    SendingMailView,
                    GetSendingListView ,
                    CheckShippingHistoryView, 
                    UnSubscribeView,
                    DelteEmailView)

urlpatterns = [
    path('subscribe', SubscribeView.as_view()),
    path('unsubscribe', UnSubscribeView.as_view()),
    path('deleteemail', DelteEmailView.as_view()),
    path('mail', SendingMailView.as_view()),
    path('inbox/<int:email_id>', GetSendingListView.as_view()),
    path('checkshipping', CheckShippingHistoryView.as_view())
]
