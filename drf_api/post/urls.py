from django.urls import path, include
from .views import *


urlpatterns = [
    

    path('post/', PostListAPIView.as_view()),
    path('post/<int:pk>/', PostUpdateAPIView.as_view()),
    path('my_post/', MyPostAPIView.as_view()),
    path('like/', LikeOrUnlikePost.as_view()),

]