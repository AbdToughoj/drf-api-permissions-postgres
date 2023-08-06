from django.shortcuts import render
from .models import Snack, Post
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SnackSerializer, PostSerializer
from rest_framework.permissions import AllowAny
from .permissions import IsPurchaserOrReadOnly

# Create your views here.

class SnackListView(ListCreateAPIView):

    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
    permission_classes = [IsPurchaserOrReadOnly]


class PostListView(ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]


class  PostDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny]

