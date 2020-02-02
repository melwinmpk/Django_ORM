from django.urls import path
from . import views


urlpatterns = [
    path('',views.login, name='index'), # HomeView views.index
    path('login',views.login, name='login'),
    path('register',views.register, name='register')
]