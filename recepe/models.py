from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Recepies(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Recepies_name=models.CharField(max_length=100)
    Recepies_description=models.TextField()
    Country=models.CharField(max_length=20)
    Dish_Image=models.ImageField(upload_to='Image')
    category = models.CharField(max_length=30, default='Other')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self)->str:
        return self.Recepies_name

    def like_count(self):
        return self.likes.count()


class Comment(models.Model):
    recipe = models.ForeignKey(Recepies, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username}: {self.text[:30]}'
    
    
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
        

    