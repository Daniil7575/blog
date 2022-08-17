from django.urls import path
from .views import PostsHome


urlpatterns = [
    path('', PostsHome.as_view(), name='home'),
]
