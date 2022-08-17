from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostsHome(ListView):
    paginate_by = 5
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/home.html'

    def get_queryset(self):
        return Post.objects.all()
