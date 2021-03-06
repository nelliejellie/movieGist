from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    phone_no = models.CharField(max_length=15, blank=False)
    description = models.TextField(max_length=400, blank=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

class VideoClips(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400, blank=False)
    link = models.CharField(max_length=100, blank=False)

class VideoClips1(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400, blank=False)
    link = models.CharField(max_length=100, blank=False)

class VideoClips2(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400, blank=False)
    link = models.CharField(max_length=100, blank=False)

class VideoClips3(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=400, blank=False)
    link = models.CharField(max_length=100, blank=False)

 
