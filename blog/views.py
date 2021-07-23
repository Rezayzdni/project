from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import ContactUsForm
from django.core.mail import send_mail


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'theList'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'theList'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    # default templateName -> <app_name>/<model>_form
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your post has been created successfully!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your post has been updated successfully!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    # default templateName -> <app_name>/<model>_confirm_delete
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class About(TemplateView):
    template_name = 'blog/about.html'


class ContactUs(View):
    form_class = ContactUsForm
    template_name = 'blog/contact_us.html'

    def get(self, request, *args, **kwargs):
        contactus_form = self.form_class()
        return render(request, self.template_name, {'contact_us_form': contactus_form})

    def post(self, request, *args, **kwargs):
        contactus_form = self.form_class(request.POST)
        if contactus_form.is_valid():
            send_mail(subject=request.POST['title'],
                      message=request.POST['content'],
                      from_email=request.POST['email'],
                      recipient_list=[settings.EMAIL_HOST_USER],
                      fail_silently=False, )
            contactus_form.save()
            messages.success(request,
                             f'Thanks for contacting us! , Our team will be in touch with you in less than 24 hours.')
            return redirect('blog-home')
        else:
            messages.error(request, f'something went wrong!')
            return render(request, self.template_name, {'contact_us_form': contactus_form})
