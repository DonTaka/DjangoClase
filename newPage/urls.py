from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path("juegos", views.juegos, name="juegos"),
]
