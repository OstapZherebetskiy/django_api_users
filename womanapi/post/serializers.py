from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Post
        
        fields = ['id', 'title', 'body', 'user']

# class PostSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Post
#         fields = ['id', 'title', 'body', 'owner']

