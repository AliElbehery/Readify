from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField(_('email address'), unique=True)
    phone= models.IntegerField(null= True)


    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']
    
    objects= CustomUserManager()

    

    def __str__(self):
        return self.email



