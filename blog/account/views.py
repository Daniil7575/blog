# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.shortcuts import render
# from django.views.generic import DetailView
from django.http import HttpRequest
from django.views.generic import ListView, UpdateView
from .forms import EditProfileFormProfileData, RegisterForm, EditProfileFormUserData
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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

@login_required
def edit_profile_view(request: HttpRequest, profile_id):
    if request.method == "POST":
        # print(request.POST)
        form_user = EditProfileFormUserData()
        form_prof = EditProfileFormProfileData()
        if form_user.is_valid() and form_prof.is_valid():

            edit_profile = form.save(commit=False)
            prof_image = form.cleaned_data['profile_image']
            prof_dob = form.cleaned_data['date_of_birth']
            edit_profile.save(commit=True)
            context = {
                'form': edit_profile,
                'image': prof_image,
                'dob': prof_dob,
            }
            return render(request, 'account/profile_edit.html', context)
    else:
        form_user = EditProfileFormUserData(instance=User.objects.get(pk=profile_id))
        form_prof = EditProfileFormProfileData(instance=Profile.objects.get(pk=profile_id))
    return render (request, 'account/profile_edit.html', {'u_form': form_user, 'p_form': form_prof})
