# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.shortcuts import render
# from django.views.generic import DetailView
from django.http import HttpRequest
from django.views.generic import ListView
from .forms import RegisterForm
from .models import Profile


# Create your views here.
# def mainpage(request):
#     return render(request, 'account/base.html', {})


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            context = {'new_user': new_user}
            return render(request, 'account/register_done.html', context)
    else:
        user_form = RegisterForm()
    return render(request, 'account/register.html', {'user_form': user_form})


# @login_required
def profile_detail(request: HttpRequest, profile_id):
    user = Profile.objects.select_related().get(user_id=profile_id)
    return render(request, 'account/profile_detail.html', {'userprof': user})
