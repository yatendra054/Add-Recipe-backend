from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import User
class Recepies(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Recepies_name=models.CharField(max_length=100)
    Recepies_description=models.TextField()
    Country=models.CharField(max_length=20)
    Dish_Image=models.ImageField(upload_to='Image')
    
class UserRecord(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    