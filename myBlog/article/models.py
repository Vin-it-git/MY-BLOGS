from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)