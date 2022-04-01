from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    Serializer_class = PostSerializer

