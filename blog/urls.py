from django.conf import settings
from django.template.context_processors import static
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
    #path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    path('contact-us/',views.contact_us,name='blog_contact_us'),
]