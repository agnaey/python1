from django.contrib.auth.models import User
from django.db import models


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True}) 




class Submission(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)
    grade = models.CharField(max_length=5, blank=True, null=True)