from django.urls import path
from . import views

urlpatterns = [

    # <--------------------- Auth Views Start ------------------------------> #
    path('home', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    # <--------------------- Auth Views End ------------------------------> #


    # <--------------------- Unauth Views Start ------------------------------> #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    # <--------------------- Unauth Views End ------------------------------> #

    


]
