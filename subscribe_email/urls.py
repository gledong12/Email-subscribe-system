from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('Email.urls')),
    path('api/v1/', include('user.urls'))
]
