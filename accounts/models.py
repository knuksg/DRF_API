from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    email = models.CharField(max_length=100, unique=True)
    mbti = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email