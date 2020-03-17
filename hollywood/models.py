from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=300)
    year_of_release = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    like_counts = models.IntegerField(default=0)
    dislike_counts = models.IntegerField(default=0)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name

class Tvshows(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=300)
    year_of_release = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    season = models.CharField(max_length=5, blank=True)
    episode = models.CharField(max_length=5, blank=True)
    like_counts = models.IntegerField(default=0)
    dislike_counts = models.IntegerField(default=0)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class gist(models.Model):    
    gists = models.TextField(max_length=300,null=True)
    gist_like_counts = models.IntegerField(default=0)
    gist_dislike_counts = models.IntegerField(default=0)
    gist_like = models.BooleanField(default=False)
    gist_dislike = models.BooleanField(default=False)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.gists

class tvshowgist(models.Model):    
    gists = models.TextField(max_length=300,null=True)
    gist_like_counts = models.IntegerField(default=0)
    gist_dislike_counts = models.IntegerField(default=0)
    gist_like = models.BooleanField(default=False)
    gist_dislike = models.BooleanField(default=False)
    tvshow = models.ForeignKey(Tvshows, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.gists