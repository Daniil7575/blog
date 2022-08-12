from django.urls import path, include
from django.contrib.auth import views
from .views import *


urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('', mainpage, name='mainpage')
]