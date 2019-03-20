from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from .models import Profile, Post

# Create your views here.


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'core/index.html', context)


def profile(request):
    context = {'profile': Profile.objects.all()}
    return render(request, 'core/profile.html', context)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'core/post_detail.html'
