from dataclasses import fields

from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Woman



class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = ('title', 'content', 'cat', 'time_create', 'time_update', 'user_id')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('last_login', 'username', 'email', 'id')






