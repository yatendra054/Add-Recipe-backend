from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Recepies(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Recepies_name=models.CharField(max_length=100)
    Recepies_description=models.TextField()
    Country=models.CharField(max_length=20)
    Dish_Image=models.ImageField(upload_to='Image')
    