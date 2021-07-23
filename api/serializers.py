from rest_framework import serializers
from blog.models import Post
from users.models import Profile
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username', )
    date_posted = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'date_posted', 'author']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    phoneNumber = serializers.CharField(required=False, write_only=True, max_length=13)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'currentLocation', 'phoneNumber']


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile']
