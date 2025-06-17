from django.db import models
from django.contrib.auth.models import AbstractUser

#CustomUserModel definition
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()
