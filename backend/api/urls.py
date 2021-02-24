from django.urls import path
from django.contrib import admin
from api import views


urlpatterns = [
    path('usuario/login', views.login_required, name='login_required'),
    path('usuario/<str:uid>/', views.user_by_uid, name='user_by_uid'),
    path('usuario/crear', views.create_user, name='create_user'),
    path('menu/reservar', views.select_menu_usuario, name='select_menu_usuario'),
    path('menu/crear', views.create_menu, name='create_menu'),
    path('menu/confirmar', views.confirmation_menu, name='confirmation_menu')

]
