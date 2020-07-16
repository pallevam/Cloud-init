from django.urls import path
from .views import homePage, loginPage, dashboard


urlpatterns = [
    path('', homePage, name='home'),
    path('loginpage', loginPage, name='login'),
    path('dashboard', dashboard, name='dashboard'),
]

