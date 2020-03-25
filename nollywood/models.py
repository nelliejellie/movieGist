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
    

    def __str__(self):
        return self.name

class gist(models.Model):    
    gists = models.TextField(max_length=300,null=True)
    movie_like = models.ManyToManyField(User, blank=True, related_name='nmovie_likes')
    movie_dislike = models.ManyToManyField(User, blank=True, related_name='nmovie_dislikes')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nollyusermovie')
    date = models.DateTimeField(default=datetime.now, blank=True)
    worth_seeing = models.CharField(max_length=20,null=True, blank=True)
    not_worth_seeing = models.CharField(max_length=20,null=True, blank=True)


    def __str__(self):
        return self.gists

class tvshowgist(models.Model):    
    gists = models.TextField(max_length=300,null=True)
    tvshow_like = models.ManyToManyField(User, blank=True, related_name='ntvshow_likes')
    tvshow_dislike = models.ManyToManyField(User, blank=True, related_name='ntvshow_dislikes')
    tvshow = models.ForeignKey(Tvshows, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='nollyusertvshow')
    date = models.DateTimeField(default=datetime.now, blank=True)
    worth_seeing = models.CharField(max_length=20,null=True, blank=True)
    not_worth_seeing = models.CharField(max_length=20,null=True, blank=True)



    def __str__(self):
        return str(self.gists)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mynollylikesuser')
    tvshow = models.ForeignKey(Tvshows, on_delete=models.CASCADE, related_name='mynollylikestvshow')
    date = models.DateTimeField(default=datetime.now, blank=True)

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mynollydislikesuser')
    tvshow = models.ForeignKey(Tvshows, on_delete=models.CASCADE, related_name='mynollydislikestvshow')
    date = models.DateTimeField(default=datetime.now, blank=True)

class MovieLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mynollylikesusermovies')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='mynollylikesmovies')
    date = models.DateTimeField(default=datetime.now, blank=True)

class MovieDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mynollydislikesusermovies')
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='mynollydislikesmovies')
    date = models.DateTimeField(default=datetime.now, blank=True)