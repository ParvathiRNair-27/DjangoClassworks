from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=30)
    description=models.TextField()
    director_name=models.CharField(max_length=100)
    language=models.CharField(max_length=20)
    year=models.IntegerField()
    image=models.ImageField(upload_to="movies")