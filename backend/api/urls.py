from django.urls import path
from django.contrib import admin
from api import views


urlpatterns = [
    path('usuario/login', views.login_required, name='make_a_order'),
    path('usuario/<str:uid>/', views.user_by_uid, name='details'),
    path('usuario/crear', views.create_user, name='create_user'),
    path('menu/reservar', views.select_menu_usuario, name='save_menu_usuario'),
    path('menu/crear', views.create_menu, name='create_menu'),
    path('menu/confirmar', views.confirmation_menu, name='confirmation_menu')

]
