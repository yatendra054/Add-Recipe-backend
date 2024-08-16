from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recepies(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Recepies_name=models.CharField(max_length=100)
    Recepies_description=models.TextField()
    Country=models.CharField(max_length=20)
    Dish_Image=models.ImageField(upload_to='Image')
class UserInformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    User_Name = models.CharField(max_length=100)
    Email = models.EmailField(null=True)
    
    def __str__(self)->str:
        return self.User_Name