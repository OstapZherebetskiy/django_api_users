from django.db import router
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from .views import *



urlpatterns = [
    

    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostUpdateAPIView.as_view()),
]