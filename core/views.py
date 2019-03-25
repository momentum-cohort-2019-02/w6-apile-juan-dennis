from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Profile, Post, Vote
from django.views.decorators.http import require_http_methods
from django.http import Http404
# Create your views here.


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'core/index.html', context)


def profile(request):
    context = {'profile': Profile.objects.all()}
    return render(request, 'core/profile.html', context)


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