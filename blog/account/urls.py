from django.urls import path
from django.contrib.auth import views
from .views import register, profile_detail


urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(template_name='account/login.html'),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(template_name='account/loggedout.html'),
        name="logout"
    ),

    path('registration/', register, name='register'),

    path('profile/<int:profile_id>/', profile_detail, name='profile_detail'),
]
