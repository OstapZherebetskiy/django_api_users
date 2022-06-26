from rest_framework import generics, viewsets, permissions
from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post

class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
