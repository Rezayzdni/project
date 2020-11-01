from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm, UserProfileForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth import forms


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Your account has been created! You are now able to login')
#             return redirect('user-login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'users/register.html', {'form': form})


# def login(request):
#     print('xxxxxxxxxxxxxxxxxxx')
#     if request.method == 'POST':
#         print('2222222222222')
#         username = request.POST['username']
#         password = request.POST['password']
#         users = User.objects.all()
#         for user in users:
#             if user.password == password and user.username == username:
#                 messages.success(request, f"You've logged in successfully!")
#                 print('1111111111')
#                 break
#     return render(request, 'users/login.html')

# def profile(request):
#     if request.method == 'POST':
#         uu_form = UserUpdateForm(request.POST,instance=request.user)
#         pu_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
#         if uu_form.is_valid() and pu_form.is_valid():
#             uu_form.save()
#             pu_form.save()
#             messages.success(request, f'Your account has been updated successfully!')
#             return redirect('user-profile')
#     else:
#         uu_form = UserUpdateForm(instance=request.user)
#         pu_form = ProfileUpdateForm(instance=request.user.profile)
#
#     context = {
#         'uu_form': uu_form,
#         'pu_form': pu_form
#     }
#     return render(request,'users/profile.html',context)

def register(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST)
        if ur_form.is_valid():
            #username = ur_form.cleaned_data.get('username')
            ur_form.save()
            messages.success(request, f'Your account has been created successfully!')
            return redirect('user-profile')

    else:
        ur_form = UserRegisterForm()
    context = {
        'ur_form': ur_form,
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('user-profile')
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = UserProfileForm(instance=request.user.profile)
    context = {
        'uu_form': uu_form,
        'pu_form': pu_form,
    }
    return render(request, 'users/profile.html', context)

# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return redirect(reverse('your_success_url'))
#         else:
#             messages.error(request, 'username or password not correct')
#             return redirect(reverse('your_login_url'))
#
#
#     else:
#         form = AuthenticationForm()
#     return render(request, 'your_template_name.html', {'form': form})
