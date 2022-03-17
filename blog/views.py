from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


def list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/list.html', {'posts': posts})


def show(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/show.html', {'post': post})
