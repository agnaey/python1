from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    quantity = models.IntegerField(default=1)

# class User(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=255)