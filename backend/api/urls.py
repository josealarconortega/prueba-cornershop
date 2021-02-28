from django.urls import path
from django.contrib import admin
from api import views


urlpatterns = [
    path('usuarios', views.obtener_usuarios, name='obtener_usuarios'),
    path('usuarios/login', views.login_required, name='login_required'),
    path('usuarios/<str:uid>/', views.user_by_uid, name='user_by_uid'),
    path('usuarios/crear', views.create_user, name='create_user'),
    path('usuarios/editar', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('usuarios/reservar', views.select_menu_usuario, name='select_menu_usuario'),
    path('usuarios/<int:usuario_id>/menus', views.obtener_menus_usuario_id_fecha, name='obtener_menus_usuario_id_fecha'),
    path('usuarios/menus', views.obtener_menus_usuario_fecha, name='obtener_menus_usuario_fecha'),
    path('menus/fecha', views.menu_by_date, name='menu_by_date'),
    path('menus/fecha/status', views.menu_by_date_status, name='menu_by_date_status'),
    path('menus/crear', views.create_menu, name='create_menu'),
    path('menus/editar', views.editar_menu, name='editar_menu'),
    path('menus/eliminar/<int:menu_id>', views.eliminar_menu, name='eliminar_menu'),
    path('menus/confirmar', views.confirmation_menu, name='confirmation_menu'),
    path('perfiles', views.obtener_perfiles, name = 'obtener_perfiles')

]
