from django.urls import path
from . import views

urlpatterns = [

    # <--------------------- Unauth Views Start ------------------------------> #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    # <--------------------- Unauth Views End ------------------------------> #

    


]
