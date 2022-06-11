from django.urls import path
from . import views



urlpatterns = [

    path("register", views.UserRegister, name="User Register"),
    path("login", views.UserLogin, name="User Login "),
    path("setting",views.UserSetting,name="User Setting"),
    path("show",views.listAllUsers, name="List of all Users"),
    path("users", views.listUsers, name="List of Individual"),
    path("experts", views.listExperts, name="List of Experts"),

]