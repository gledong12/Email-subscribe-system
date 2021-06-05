from django.urls import path
from .views import SubscribeView, SendingMailView, GetSendingListView ,CheckShippingHistoryView

urlpatterns = [
    path('subscribe', SubscribeView.as_view()),
    path('mail', SendingMailView.as_view()),
    path('inbox/<int:email_id>', GetSendingListView.as_view()),
    path('check', CheckShippingHistoryView.as_view())
]
