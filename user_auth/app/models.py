from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Designation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    profile_photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True, related_name="employees")
    
    password = models.CharField(max_length=255)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

