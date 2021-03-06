import requests

from django.http import response
from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import (
    MovieSerializer,
    RatingSerializer, 
    MovieListSerializer,
    CommentSerializer,
    ReplySerializer)
from .models import Movie, Comment, MovieList, Rating, Reply


@api_view(['GET'])
def movie_list(request):
    data = []
    for i in range(1, len(MovieList.objects.values('list_id').distinct())+1):
        movies = MovieList.objects.filter(list_id=i)
        data.append(MovieListSerializer(movies, many=True).data)
    return Response(data)


@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def movie_list_create(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        for data in request.data:
            data = {
                'title': data['title'],
                'genre': str(data['genre_ids']),
                'overview': data['overview'],
                'backdrop_path': data['backdrop_path'],
                'poster_path': data['poster_path'],
                'vote_average': data['vote_average']
            }
            serializer = MovieSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def likes(request, movie_id):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, movie_id=movie_id)
        if movie.like_users.filter(pk=request.user.pk).exists():
        # if request.user in article.like_users.all():
            # ????????? ??????
            movie.like_users.remove(request.user)
            liked = False
        else:
            # ????????? ??????
            movie.like_users.add(request.user)
            liked = True
        return Response({ 'liked': liked },status=status.HTTP_200_OK)
    return Response( status=status.HTTP_418_IM_A_TEAPOT)


@api_view(['GET'])
def review_list(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    serializer = CommentSerializer(movie.comment_set, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    request.data['username'] = request.user.username
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if not request.user.comment_set.filter(pk=comment_pk).exists():
        return Response({ 'detail' : '????????? ????????????'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({ 'id': comment_pk })


@api_view(['GET'])
def reply_list(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializers = ReplySerializer(comment.reply_set, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def reply_create(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(comment=comment, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def reply_update_delete(request, reply_pk):
    reply = get_object_or_404(Reply, pk=reply_pk)
    if not request.user.reply_set.filter(pk=reply_pk).exists():
        return Response({ 'detail' : '????????? ????????????'}, status=status.HTTP_403_FORBIDDEN)
    if request.method == 'PUT':
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        reply.delete()
        return Response({ 'id': reply_pk })


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_rate(request, movie_id):
    movie = get_object_or_404(Movie, movie_id=movie_id)
    if Rating.objects.filter(movie_id=movie.pk, user_id=request.user.pk).exists():
        rating = get_object_or_404(Rating, pk=Rating.objects.filter(movie_id=movie.pk, user_id=request.user.pk).values('id')[0].get('id'))
        serializer = RatingSerializer(rating, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    else:
        serializers = RatingSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save(movie=movie, user=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
def review_user(request):
    data = {
        'user_id': request.user.id
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
def reply_user(request):
    data = {
        'user_id': request.user.id
    }
    return Response(data, status=status.HTTP_200_OK)




# movie db?????????.
# def tmp(request):
#     dic = {}
#     for i in range(1, 11):
#         url = 'https://api.themoviedb.org/3/list/' + str(i) + '?api_key=f361f3c50ed76f4dd96355b1957b3f29&language=ko-kr'
#         response = requests.get(url)
#         tmp = response.json()
#         for data in tmp.get('items'):
#             url2 = 'https://api.themoviedb.org/3/movie/' + str(data.get('id')) + '?api_key=f361f3c50ed76f4dd96355b1957b3f29&language=ko-kr&append_to_response=videos'
#             response2  = requests.get(url2)
#             tmp2 = response2.json()
#             movieId = tmp2.get('id')
#             if str(movieId) in dic.keys():
#                 continue
#             dic[f'{movieId}'] = 1
#             data = {
#                 'movie_id': movieId,
#                 'title': tmp2.get('title'),
#                 'release_date': tmp2.get('release_date'),
#                 'overview': tmp2.get('overview'),
#                 'tagline': tmp2.get('tagline'),
#                 'backdrop_path': tmp2.get('backdrop_path'),
#                 'poster_path': tmp2.get('poster_path'),
#                 'vote_average': tmp2.get('vote_average')
#             }
#             if len(tmp2.get('videos').get('results')) > 0:
#                 data['trailer'] = tmp2.get('videos').get('results')[0].get('id')
#             genre_tmp = ''
#             for genre in tmp2.get('genres'):
#                 genre_tmp += str(genre.get('id'))
#                 genre_tmp += ','
#             data['genre'] = genre_tmp
#             serializer = MovieSerializer(data=data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()


# movielist db ?????????
# def tmp(request):
#     dic = {}
#     for i in range(1, 11):
#         url = 'https://api.themoviedb.org/3/list/' + str(i) + '?api_key=f361f3c50ed76f4dd96355b1957b3f29&language=ko-kr'
#         response = requests.get(url)
#         tmp = response.json()
#         for data in tmp.get('items'):
#             movieId = data.get('id')
#             print(movieId)
#             if str(movieId) in dic.keys():
#                 continue
#             dic[f'{movieId}'] = 1
#             list_id = int(tmp.get('id'))
#             if list_id > 5:
#                 list_id -= 1
#             data = {
#             'list_id': list_id,
#             'movie_id': movieId,
#             'description': tmp.get('description'),
#             }
#             serializer = MovieListSerializer(data=data)
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save()