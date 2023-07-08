from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag

# Create your views here.

all_posts = Post.objects.all()


def starting_page(request):
    latest_posts = all_posts.order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    updated_posts = all_posts.order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })


def post_detail(request, slug):

    updated_posts = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": updated_posts,
        "post_tags": updated_posts.tags.all()
    })
