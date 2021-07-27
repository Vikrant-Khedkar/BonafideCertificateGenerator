from django.db import models

# Create your models here.
class Submit(models. Model):
    name = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    division = models.CharField(max_length=30)
    rollno = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    enroll = models.CharField(max_length=30)
def __str__(self):
    return self.name