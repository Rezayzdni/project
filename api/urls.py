from django.urls import path
from .views import (ListCreatePost, RetrieveUpdateDestroyPost, ListUser,
                    RetrieveUser, ListCreateUserPost,RetrieveUpdateDestroyUserPost,
                    RetrieveUpdateProfile, ListProfile)

urlpatterns = [
    path('users/', ListUser.as_view(), name='user-list-drf'),
    path('users/<int:pk>', RetrieveUser.as_view(), name='user-detail-drf'),
    path('users/<int:pk>/posts', ListCreateUserPost.as_view(), name='user-posts-drf'),
    path('users/<int:pk>/posts/<int:post_pk>', RetrieveUpdateDestroyUserPost.as_view(), name='user-posts-detail-drf'),
    path('posts/', ListCreatePost.as_view(), name='post-list-drf'),
    path('posts/<int:pk>', RetrieveUpdateDestroyPost.as_view(), name='post-detail-drf'),
    path('profiles/', ListProfile.as_view(), name='profile-list-drf'),
    path('profiles/<int:pk>', RetrieveUpdateProfile.as_view(), name='profile-detail-drf')
]
