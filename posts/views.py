from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
posts = [
    {
        "id": 1,
        "title": "First Post",
        "content": "This is the content of the first post.",
    },
    {
        "id": 2,
        "title": "Second Post",
        "content": "This is the content of the second post.",
    },
    {
        "id": 3,
        "title": "Third Post",
        "content": "This is the content of the third post.",
    },
]


def home(request):
    return render(request, "posts/home.html", {"posts": posts, "username": "vu duc"})


def post_detail(request, post_id):
    valid_id = False
    for post in posts:
        if post["id"] == post_id:
            post_dict = post
            valid_id = True
            break
    if valid_id:
        return render(request, "posts/post.html", {"post": post_dict})
    else:
        return HttpResponseNotFound("<h1>Post not found</h1>")


def redirect_to_detail(request, post_id):
    return HttpResponseRedirect(f"{reverse('post_detail', args=[post_id])}")
