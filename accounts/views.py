from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def register(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['confirm_password']:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=request.POST['email']).exists():
                messages.info(request, "Email already taken")

            else:
                user = User.objects.create_user(username=request.POST['username'],
                                                email=request.POST['email'],
                                                first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'],
                                                password=request.POST['password'])
                user.save()
                messages.success(request, "User Created")
                return redirect('accounts:login')
        else:
            messages.info(request, "Password does not match")
            return redirect('accounts:register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('poll:all_polls')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
