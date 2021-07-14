from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USERNAME_FIELD = "email"
    email = models.EmailField(("email address"), unique=True) 
    REQUIRED_FIELDS = ["username"] 
    def __str__(self):
        return self.username
