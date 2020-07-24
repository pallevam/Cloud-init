from django.shortcuts import render
from django.http import HttpResponse

def homePage(request):
    return render(request, 'home.html')

def loginPage(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')






