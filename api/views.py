from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from blog.models import Post
from users.models import Profile
from .serializers import PostSerializer, ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,
                                     ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from .permissions import IsOwnerOrReadOnly


class ListUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUser(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(User.objects.all(),
                                id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class ListCreatePost(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListCreateUserPost(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        return self.queryset.filter(author=user)

    def perform_create(self, serializer):
        user = get_object_or_404(User, id=self.kwargs.get('pk'))
        if self.request.user == user:
            serializer.save(author=user)
        else:
            raise PermissionDenied


class RetrieveUpdateDestroyUserPost(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(Post.objects.all(),
                                author_id=self.kwargs.get('pk'),
                                id=self.kwargs.get('post_pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(Post.objects.all(),
                                id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj


class ListProfile(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class RetrieveUpdateProfile(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self):
        obj = get_object_or_404(Profile.objects.all(),
                                id=self.kwargs.get('pk'))
        self.check_object_permissions(self.request, obj)
        return obj
