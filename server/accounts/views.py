from .models import User
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# from server.accounts import serializers


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 , 장고에 내장되어 있는 함수. 패스워드 암호화하는 함수.
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    like_movies = []
    # 여기는 돌려보지 못했다. request로 현재 유저 이름 데이터를 보내줘야 한다.
    person = get_object_or_404(get_user_model(), username=request.data.get('username'))
    tmp = person.like_movies.all()
    for lm in tmp:
        data1 = {
            'title': lm.title,
            'genre': lm.genre,
            'tagline': lm.tagline,
            'backdrop_path': lm.backdrop_path,
            'poster_path': lm.poster_path,
            'vote_average': lm.vote_average,
            'movie_id': lm.movie_id
        }
        like_movies.append(data1)

    data2 = {
        'person': person.pk,
        'movie': like_movies
    }
    print(data2)
    return Response(data2, status=status.HTTP_201_CREATED)
    # return Response(status=status.HTTP_201_CREATED)