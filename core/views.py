from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Profile, Post, Vote, Comment
from django.views.decorators.http import require_http_methods
from django.http import Http404
from .forms import PostForm, CommentForm
from . import forms

# Create your views here.


def home(request):

    context = {'post': Post.objects.all()}
    return render(request, 'index.html', context)


# class HomeView(generic.DetailView):
#     model = Post
#     template_name = 'core/index.html'


def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments_post.all()
    context = {'post': post, 'comments': comments}
    return render(request, 'core/post_detail.html', context)


def get(self, request):
    form = HomeForm()
    return render(request.self.template_name, {'form': form})


# class PostDetailView(generic.DetailView):
#     model = Post
#     template_name = 'core/post_detail.html'


def profile(request):
    context = {'profile': Profile.objects.all()}
    return render(request, 'core/profile.html', context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('core-home')
    else:
        form = PostForm()
    return render(request, 'core/create_post.html', {'form': form})


class PostDetailView(generic.DetailView):
    model = Post


@require_http_methods(['POST'])
@login_required
def vote_on_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    profile = request.user.profile
    vote, created = Vote.objects.get_or_create(post=post, profile=profile)
    if not created:
        vote.delete()
    print(created)
    return redirect('core-home')


@login_required
def create_comment(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user=request.user)
            comment.post = Post.objects.get(id=pk)
            comment.save()
            return redirect('post_new')
    else:
        form = CommentForm()
    return render(request, 'core/create_post.html', {'form': form})
