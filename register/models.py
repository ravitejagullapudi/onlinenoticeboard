from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    branch = models.CharField(max_length=4)
    year = models.CharField(max_length=3)
    sec = models.CharField(max_length=3)
