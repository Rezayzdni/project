from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.forms import DateInput

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','first_name', 'email', ]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phoneNumber', 'currentLocation']
        widgets = {
            'image': forms.FileInput(),
        }
        labels = {
            'image': 'Profile Photo',
        }

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', ]
#
#
# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image', 'phoneNumber']

# class UserLoginForm(auth_views):
# print('xxxxxxxxxxxxxxxxxxx', request.method)
# if request.method == 'POST':
#     print('2222222222222')
#     username = request.POST['username']
#     password = request.POST['password']
#     users = User.objects.all()
#     for user in users:
#         if user.password == password and user.username == username:
#             messages.success(request, f"You've logged in successfully!")
#             print('1111111111')
#             break
