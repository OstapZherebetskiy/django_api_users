from dataclasses import fields
from email.policy import default
from requests import post
from .models import Post
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']
