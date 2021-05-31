from django.shortcuts import render


def home(request):
    return render(request, 'base.html')


def user_account(request):
    return render(request, 'users/profile.html')
