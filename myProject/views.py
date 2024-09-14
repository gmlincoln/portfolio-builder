from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout 


from myApp.models import *

def dashboardPage(req):

    user = req.user

    context = {
        'user': user
    }

    return render(req, 'myAdmin/index.html', context) 


def registerPage(req):

    if req.method == 'POST':
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        

        if password == confirm_password:
            register_user = Custom_User.objects.create_user(
                user_type = req.POST.get('user_type'),
                first_name = req.POST.get('first_name'),
                last_name = req.POST.get('last_name'),
                username = req.POST.get('username'),
                email = req.POST.get('email'),
                password = confirm_password 

            )
            register_user.save()
            return redirect('loginPage')
    
    return render(req, 'common/register.html')


def loginPage(req):

    if req.method == 'POST':
        user_name = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(req, username = user_name, password = password)

        if user:
            login(req,user)
            return redirect('dashboardPage')
        else:
            return HttpResponse('Incorrect username or password. Please try again.')
            

    return render(req, 'common/login.html')


def logoutPage(req):

    logout(req)

    return render(req, 'common/login.html')