from django.urls import path, include
from django.contrib.auth import views
from .views import *


urlpatterns = [
    path('authentication/', views.LoginView.as_view(), name='login'),
    path('', mainpage, name='mainpage')
]