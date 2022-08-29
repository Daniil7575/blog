from django.http import HttpRequest
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.contrib import messages

from django.forms import ModelForm

from .models import Post
from .forms import CommentForm, PostForm


class PostsHome(ListView):
    paginate_by = 5
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/home.html'

    def get_queryset(self):
        return Post.objects.all()


class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'posts/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
    form_class = CommentForm

    def get_success_url(self) -> str:
        return reverse('post_detail', kwargs={'post_slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['post'].comments.all()
        print(context['comments'])
        context['form'] = CommentForm()
        return context

    def post(self, request: HttpRequest, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('account:login', permanent=True)

        self.object = self.get_object()
        form = self.get_form()
        
        if form.is_valid():
            return self.form_valid(form, request.user.username)
        else:
            return self.form_invalid(form)

    def form_valid(self, form: ModelForm, username):
        comment = form.save(commit=False)
        comment.name = username
        comment.post = self.object
        comment.save()
        return super(PostDetail, self).form_valid(comment)


class PostCreationView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    template_name = 'posts/post_create_form.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.slug = slugify(self.request.POST['title'])
        post.author = self.request.user
        post.save()
        return super(PostCreationView, self).form_valid(form)
