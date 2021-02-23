from django.urls import path
from django.contrib import admin
from api import views


urlpatterns = [
    path('usuario/login', views.save_menu, name='make_a_order'),
    path('menu/reservar', views.select_menu_usuario, name='save_menu_usuario')

]
