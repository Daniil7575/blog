from django.urls import path
from .views import PostsHome, PostDetail, PostCreationView


urlpatterns = [
    path('', PostsHome.as_view(), name='home'),
    path(
        '<slug:post_slug>',
        PostDetail.as_view(), 
        name='post_detail'
    ),
    path(
        'create/',
        PostCreationView.as_view(),
        name='post_create'
    ),
]
