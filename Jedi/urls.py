from django.urls import path
from .views import homePage, loginPage, signup, logout_request, dashboard


urlpatterns = [
    path('', homePage, name='home'),
    path('loginpage', loginPage, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout_request, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
]

