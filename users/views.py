from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.base import View
from .form import UserRegistrationForm, UserProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


class Register(View):
    form_class = UserRegistrationForm
    template_name = 'users/register.html'

    def get(self,request, *args, **kwargs):
        ur_form = self.form_class()
        return render(request, self.template_name, {'ur_form': ur_form})

    def post(self,request, *args, **kwargs):
        ur_form = self.form_class(request.POST)
        if ur_form.is_valid():
            ur_form.save()
            messages.success(request, f'Your account has been created successfully!')
            return redirect('user-profile')
        else:
            return render(request, self.template_name, {'ur_form': ur_form})


@login_required
def profile(request):
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():#don forget to provide else statement
            uu_form.save()
            pu_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return render(request, 'users/profile.html', {'uu_form': uu_form, 'pu_form': pu_form,})
    else:
        uu_form = UserUpdateForm(instance=request.user)
        pu_form = UserProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'uu_form': uu_form, 'pu_form': pu_form,})