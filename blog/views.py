from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, ContactUs
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .form import ContactUsForm
from django.core.mail import send_mail


# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         'title': 'Home'
#     }
#
#     return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
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
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def contact_us(request):
    if request.method == 'POST':
        c_u_form = ContactUsForm(request.POST)
        if c_u_form.is_valid():
            # title = c_u_form.cleaned_data.get('title')
            send_mail(subject=request.POST['title'],
                      message=request.POST['content'],
                      from_email=request.POST['email'],
                      recipient_list=[settings.EMAIL_HOST_USER],
                      fail_silently=False,
                      )
            c_u_form.save()
            messages.success(request,
                             f'thanks for contacting us! , our team will be in touch with you in less than 24 hours.')
            return redirect('blog-home')
        else:
            messages.ERROR(request, f'something went wrong!')
    c_u_form = ContactUsForm()
    return render(request, 'blog/contact_us.html', {'contact_us_form': c_u_form})
