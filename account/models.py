from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userInfo(models.Model):
    user_info = models.OneToOneField(User,related_name="user_info")
    tel = models.CharField(null=False,max_length=11)
    token = models.CharField(max_length=128,null=True,blank=True)
    ip = models.GenericIPAddressField(null=True,blank=True)
    start_time = models.DateTimeField(null=True,blank=True)
    end_time = models.DateTimeField(null=True,blank=True)
    create_time = models.DateTimeField(null=True,blank=True)
    modify_time = models.DateTimeField(null=True,blank=True)
#class userinfo_service(models.Model):







