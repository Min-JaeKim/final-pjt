from django.db import models
from django.conf import settings
from django.db.models.fields import FloatField

# Create your models here.

class MovieList(models.Model):
    list_id = models.IntegerField()
    movie_id = models.IntegerField()
    description = models.TextField(blank=True)


class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    movie_id = models.IntegerField()
    title = models.CharField(max_length=100, blank=True)
    genre = models.TextField(blank=True)
    release_date = models.TextField(blank=True)
    overview = models.TextField(blank=True)
    tagline = models.CharField(max_length=100, blank=True)
    trailer = models.TextField(blank=True, null=True)
    backdrop_path = models.TextField(blank=True)
    poster_path = models.TextField(blank=True)
    vote_average = models.FloatField(blank=True)


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.FloatField(blank=True, null=True)


class Favorite(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
