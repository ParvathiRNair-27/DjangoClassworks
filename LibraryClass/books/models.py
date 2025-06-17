from django.db import models

# Create your models here.
# model definition (database scheme)
class books(models.Model):
    Title=models.CharField(max_length=200)
    Author = models.CharField(max_length=200)
    Price=models.IntegerField()
    Language=models.CharField(max_length=200)
    Pages=models.IntegerField()
    Image=models.ImageField(upload_to="books")