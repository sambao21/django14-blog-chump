from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from posts.models import Post


def home(request):
    return render_to_response("home.html", {"posts": Post.objects.all().order_by('post_date')})


def post_specific(request, post_id):
    p = get_object_or_404(Post, pk=post_id)

    return render_to_response("post_specific.html", {"post": p})
