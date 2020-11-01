from django.db import models
from django.contrib.auth.models import User
from django.views import defaults
from stdimage import StdImageField
from django import forms


# from PIL import Image
# class NotClearableImageField(forms.ImageField):
#     widget = forms.FileInput
#
#
# class MyStdImageField(StdImageField):
#     def formfield(self, **kwargs):
#         kwargs.update({'form_class': NotClearableImageField})
#         return super(MyStdImageField, self).formfield(**kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.thumbnail.jpg',upload_to='profile_pics')
    image = StdImageField(default='default.jpg', upload_to='profile_pics', variations={
        'thumbnail': {"width": 300, "height": 300, }
    }, blank=True, null=False)
    # image = ResizedImageField(size=[300, 300], upload_to='profile_pics')
    currentLocation = models.CharField(max_length=25, blank=True, default='-')
    phoneNumber = models.CharField(max_length=11, blank=True, default='-')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self,*args, **kwargs):
    #     super().save()
    #     image.save(self.image.path)
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
