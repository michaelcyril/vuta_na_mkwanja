from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        username = self.validated_data['username']
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email,
                                        password=password)
        return user
