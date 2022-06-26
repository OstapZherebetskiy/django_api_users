from rest_framework import generics, viewsets, permissions
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import WomenSerializer, UserSerializer
from .models import Woman

class WomanAPIView(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomenSerializer

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]





