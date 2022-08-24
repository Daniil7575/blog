from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.shortcuts import render
from django.urls import reverse

from django.forms import ModelForm

from .models import Post
from .forms import CommentForm


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
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
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


# @login_required
# def comment_form(request: HttpRequest):
#     if request.method == 'POST':
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             new_comment = comment.save(commit=False)
#             new_comment['name'] = request.user.username
#             new_comment.save()
#             return render(
#                 request, 
#                 'posts/comment_form.html', 
#                 {'new_comment': new_comment}
#             )
#     else:
#         comment_form = CommentForm()
#     return render(
#         request, 
#         'posts/comment_form.html',
#         {'form': comment_form}
#     )
