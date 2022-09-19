from django.shortcuts import render

from posts.models import Post
from posts.models import Comment


def main(request):
    posts = Post.objects.all()
    comment = Comment.objects.all()

    data = {
        'posts': posts
    }

    return render(request, 'main.html', context=data)

