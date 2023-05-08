from django.urls import path
from . import views

urlpatterns = [

    # <--------------------- Auth URLs Start ------------------------------> #
    
    path('home', views.home, name="home"),
    path('profile', views.profile, name="profile"),
    path('continue', views.cont, name="cont"),
    path('logout', views.logout, name="logout"),
    
    # <---------- Sub URL Views For Courses in Auth Start -----------------> #
    path('courses/<str:slug>/', views.det, name="det"),
    path('courses/technology', views.tech, name="tech"),
    path('courses/eart-and-climate', views.earth, name="earth"),
    path('courses/buiness', views.business, name="business"),
    path('courses/health', views.health, name="health"),
    path('courses/law', views.law, name="law"),
    path('courses/marine', views.marine, name="marine"),
    path('courses/nationalism', views.nationalism, name="nationalism"),
    # <---------- Sub URL Views For Courses in Auth End -----------------> #

    # <--------------------- Auth URLs End ------------------------------> #


    # <--------------------- Unauth URLs Start ------------------------------> #
    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    # <--------------------- Unauth URLs End ------------------------------> #

    
]
