from django.db   import models
from user.models import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'categories'
    
class Email(models.Model):
    subject    = models.CharField(max_length=100)
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    sender     = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='sender')
    receiver   = models.ManyToManyField('user.User', through='UserEmail', related_name='receiver')
    
    class Meta:
        db_table = 'emails'
        
class UserCategory(models.Model):
    user     = models.ForeignKey('user.User', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'subscribe'
        
class UserEmail(models.Model):
    user  = models.ForeignKey('user.User', on_delete=models.CASCADE)
    email = models.ForeignKey('Email', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'receive_user'