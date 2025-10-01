from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recepies(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Recepies_name=models.CharField(max_length=100)
    Recepies_description=models.TextField()
    Country=models.CharField(max_length=20)
    Dish_Image=models.ImageField(upload_to='Image')
    
    def __str__(self)->str:
        return self.Recepies_name
    
    
class UserInformation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    User_Name = models.CharField(max_length=100)
    Email = models.EmailField(null=True)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    
    followers=models.ManyToManyField(User,related_name="following",blank=True)
    
    def __str__(self)->str:
        return self.User_Name
    
    def follower_count(self):
        return self.followers.count()
    
    def following_count(self):
        return self.user.following.count()
        

    