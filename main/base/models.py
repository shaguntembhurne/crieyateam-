from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomerClass(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']