from django.db import models

# Create your models here.
#Model definition (database schema)
class Books(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=50)
    Price=models.IntegerField()
    Pages=models.IntegerField()
    Language=models.CharField(max_length=10)
    Image=models.ImageField(upload_to="Books")

#