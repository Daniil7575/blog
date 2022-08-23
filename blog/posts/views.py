from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostsHome(ListView):
    paginate_by = 5
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/home.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['post'].comments.all()
        return context
