from django.db import models
from django.contrib.auth.models import User
from django.views import defaults
from stdimage import StdImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = StdImageField(default='default.jpg', upload_to='profile_pics', variations={
        'thumbnail': {"width": 300, "height": 300, }
    }, blank=True, null=False)
    currentLocation = models.CharField(max_length=25, blank=True, default='-')
    phoneNumber = models.CharField(max_length=11, blank=True, default='-')

    def __str__(self):
        return f'{self.user.username} Profile'