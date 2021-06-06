from django.urls import path
from .views import (SubscribeView, 
                    SendingMailView,
                    CheckingSubscriberView, 
                    GetSendingListView ,
                    CheckShippingHistoryView, 
                    UnSubscribeView)

urlpatterns = [
    path('subscribe', SubscribeView.as_view()),
    path('unsubscribe', UnSubscribeView.as_view()),
    path('checksubscribe', CheckingSubscriberView.as_view()),
    path('mail', SendingMailView.as_view()),
    path('inbox/<int:email_id>', GetSendingListView.as_view()),
    path('checkshipping', CheckShippingHistoryView.as_view())
]
