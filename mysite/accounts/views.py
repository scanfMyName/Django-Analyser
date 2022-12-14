from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import admin, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .models import Profile
# Create your views here.


def login_page(req):
    if (req.method == 'POST'):
        username = req.POST.get('username')
        password = req.POST.get('password')
        user_obj2 = User.objects.filter(username=username)
        if not user_obj2.exists():
            print("User haven't registered yet, please register first")
            messages.error(
                req, "User haven't registered yet, please register first")
            return HttpResponseRedirect(req.path_info)
        
        if user_obj2[0].profile.is_mail_verified == False:
            print("User haven't verified yet, please verify first")
            messages.error(
                req, "User haven't verified yet, please verify first")
            return HttpResponseRedirect(req.path_info)
        
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(req, "Password do not match")
            return HttpResponseRedirect(req.path_info)

    return render(req, 'accounts/login.html')


def register_page(req):
    if (req.method == 'POST'):
        first_name = req.POST.get('first_name')
        last_name = req.POST.get('last_name')
        username = req.POST.get('username')
        email = req.POST.get('email')
        password = req.POST.get('password')
        conf_password = req.POST.get('conf_password')
        if (password != conf_password):
            messages.error(req, 'Confirm password and password do not match')
            return HttpResponseRedirect(req.path_info)
        user_obj1 = User.objects.filter(username=username)
        user_obj2 = User.objects.filter(email=email)
        if (user_obj1.exists()):
            print("User already exists")
            messages.error(
                req, "A user with the same username is already exists, Please try another username")
            return HttpResponseRedirect(req.path_info)
        elif (user_obj2.exists()):
            print("Email already exists")
            messages.error(
                req, "A user with the same email is already exists, Please try another email")
            return HttpResponseRedirect(req.path_info)
        else:
            user_obj = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(
                req, "A email has been sent on your email address, Please verify your email address")

        print(req.POST)
    return render(req, 'accounts/register.html')


def activate_email(request, email_token):
    try:
        user = Profile.objects.get(email_token = email_token)
        user.is_mail_verified = True
        user.save()
        # messages.success(request, "Your email has been verified, Please login")
        return redirect('/')
    except Exception as e:
        print(e)
        # messages.error(request, "Your email has not been verified, Please try again")
        return HttpResponse("Invalid Token")