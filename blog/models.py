from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return f'title: {self.title}'


class ContactUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    email = models.EmailField()
