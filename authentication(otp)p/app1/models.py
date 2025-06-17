from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# Custom User Model
class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    address=models.TextField(default=" ")

    role=models.CharField(max_length=20,default=" ")

    is_verified=models.BooleanField(default=False) # after verification it will set true
    otp=models.CharField(max_length=10,null=True,blank=True) # to store the generated otp in backend table

    def generate_otp(self):
        # for creating random otp number for verification

        otp_number=str(randint(1000,9999))+str(self.id)
        self.otp=otp_number
        self.save()