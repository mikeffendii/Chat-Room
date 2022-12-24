from django.urls import path
from . import views

urlpatterns = [
    #path('',views.index, name = 'index'),
    path('signup/',views.signup),
    path('home/',views.home, name="home"),
    path('room/',views.room, name="room"),

]