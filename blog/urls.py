from django.urls import path
from . import views
from .views import PostListView ,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView


urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/update/<int:pk>/',PostUpdateView.as_view(),name='post-update'),
    path('post/delete/<int:pk>/',PostDeleteView.as_view(),name='post-delete'),
    path('about/', views.About.as_view(),name='blog-about'),
    path('contact-us/',views.ContactUs.as_view(),name='blog-contact-us'),
]