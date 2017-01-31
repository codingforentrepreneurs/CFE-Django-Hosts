from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import Post


def post_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")
    context = {
        "object_list": queryset_list, 
    }
    return render(request, "posts/list.html", context)



def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance": instance,
    }
    return render(request, "posts/detail.html", context)
