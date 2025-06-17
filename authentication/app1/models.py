from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    phone=models.IntegerField()
    address=models.TextField()

# Create your models here.
