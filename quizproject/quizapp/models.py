from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class Signin(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=22,unique=True,blank=True,null=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='images',blank=True,null=True)
    password = models.CharField(max_length = 150)
    
    
    def __str__(self):
        return self.first_name
    
    
    