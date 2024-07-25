from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    email=models.EmailField()
    address = models.CharField(max_length=255)
    
class Car(models.Model):
    car_name=models.CharField(max_length=15)
    speed=models.IntegerField()
    Cost=models.IntegerField()
    
    def __str__(self) -> str:
        return self.car_name
    