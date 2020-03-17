from django.db import models
from datetime import datetime

# Create your models here.

class Gist(models.Model):
    gists = models.TextField()
    gistImage = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    likes_counts = models.IntegerField(default=0)
    dislikes_counts = models.IntegerField(default=0)
    gistDate = models.DateTimeField(default=datetime.now, blank=True)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

class tvshowGist(models.Model):
    gists = models.TextField()
    gistImage = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    likes_counts = models.IntegerField(default=0)
    dislikes_counts = models.IntegerField(default=0)
    gistDate = models.DateTimeField(default=datetime.now, blank=True)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)