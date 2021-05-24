from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # write_only는 시리얼 라이징만 하고 응답에는 포함시키지 않음.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
