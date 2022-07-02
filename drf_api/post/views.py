from requests import request
from .models import Like, Post
from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializers import PostSerializer, RegisterSerializer, LikeSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .permisions import IsOwnerOrReadOnly

from rest_framework.response import Response
from rest_framework import status


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]


class MyPostAPIView(ListAPIView):
    def get_queryset(self):

        user = self.request.user
        return Post.objects.filter(user=user)

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LikeOrUnlikePost(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        post_id = request.GET.get('post_id')

        if post_id:
            like = Like.objects.filter(post = post_id).count()
            return Response(data=like, status=status.HTTP_200_OK)

        like = Like.objects.all()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            post_id = request.data['post_id']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            post = Post.objects.get(id=post_id)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(username=request.user)

        Like.objects.get_or_create(user=user, post=post)

        return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        post_id = request.GET.get('post_id')

        if post_id:
            try:
                like = Like.objects.get(user=request.user, post=post_id)
                like.delete()
            except Exception:
                return Response(status=status.HTTP_404_NOT_FOUND)

            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

