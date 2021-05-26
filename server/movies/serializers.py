from django.urls.conf import include
from rest_framework import serializers
from .models import Movie, Comment, Rating, Favorite, MovieList, Reply


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieList
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('movie_id', 'title', 'genre', 'release_date', 'overview', 'tagline', 'trailer', 'backdrop_path', 'poster_path', 'vote_average')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('content', 'created_at')


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = ('content', 'created_at')


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('rate',)


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ()