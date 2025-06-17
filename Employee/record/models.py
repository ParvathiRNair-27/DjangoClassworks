from django.db import models
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Age=models.IntegerField()
    Salary=models.IntegerField()
    Designation=models.CharField(max_length=50)
    Place=models.CharField(max_length=50)
    Image=models.ImageField(upload_to="record")
    Department_Name=models.CharField(max_length=50)

# Create your models here.
