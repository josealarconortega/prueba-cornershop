from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from api.infrastructure.repositories import DjangoORMUsuarioMenusRepository
from api.domain.entities import (
    Perfil,
    Usuario,
    Menu,
    UsuarioMenu
)
from api.models import (
    Menu as MenuModel,
    Usuario as UsuarioModel,
    Status as StatusModel,
    Perfil as PerfilModel,
    UsuarioMenu as UsuarioMenuModel
)

from datetime import date, datetime

@pytest.fixture()
def menu_usuario_model_create() -> UsuarioMenuModel:
    perfil_mantencion = PerfilModel.objects.create(descripcion = 'Mantencion')
    perfil_empleado = PerfilModel.objects.create(descripcion = 'Usuario')
    status = StatusModel.objects.create(descripcion = 'Registrado')
    usuario_created = UsuarioModel.objects.create(
        rut = '11.111.111-1', nombre = 'test', email = 'test@test.cl', fecha_registro = date.today(), 
        uid = 'qwertyqw', perfil = perfil_mantencion, password = 'test'
    )
    usuario_empleado = UsuarioModel.objects.create(
        rut = '22.222.222-2', nombre = 'test2', email = 'tes2t@test.cl', fecha_registro = date.today(),
        uid = 'qwertyqw2', perfil = perfil_empleado, password = 'test2')
    menu = MenuModel.objects.create(
        descripcion = 'Menu', entrada = 'entrada', ensalada = 'ensalada', plato_fondo = 'plato', postre = 'postre', 
        fecha_registro = date.today(), usuario_creacion = usuario_created, fecha_menu = date.today(), status = status, orden = 1
    )
    usuario_menu = UsuarioMenuModel.objects.create(usuario = usuario_empleado, menu = menu, fecha_registro = date.today())
    return usuario_menu


@pytest.mark.usefixtures('transactional_db')
def test_gets_all_existing_menu_by_date(menu_usuario_model_create: UsuarioMenuModel) -> None:
    menus = DjangoORMUsuarioMenusRepository().get_menu_by_usuario_id(menu_usuario_model_create.usuario.id, date.today())
    assert menus[0].id == menu_usuario_model_create.menu.id
    assert menus[0].descripcion == menu_usuario_model_create.menu.descripcion
    assert menus[0].entrada == menu_usuario_model_create.menu.entrada
    assert menus[0].ensalada == menu_usuario_model_create.menu.ensalada
    assert menus[0].plato_fondo == menu_usuario_model_create.menu.plato_fondo
    assert menus[0].postre == menu_usuario_model_create.menu.postre
    assert menus[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_model_create.menu.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].usuario_creacion_id == menu_usuario_model_create.menu.usuario_creacion.id
    assert menus[0].fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_model_create.menu.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].status_id == menu_usuario_model_create.menu.status.id
    assert menus[0].orden == menu_usuario_model_create.menu.orden

@pytest.mark.usefixtures('transactional_db')
def test_gets_all_existing_menu_by_user(menu_usuario_model_create: UsuarioMenuModel) -> None:
    menus = DjangoORMUsuarioMenusRepository().get_menu_usuario_by_fecha(date.today())
    assert menus[0].id == menu_usuario_model_create.id
    assert menus[0].usuario_id == menu_usuario_model_create.usuario_id
    assert menus[0].menu_id == menu_usuario_model_create.menu_id
    assert menus[0].observacion == menu_usuario_model_create.observacion
    assert menus[0].menu.id == menu_usuario_model_create.menu.id
    assert menus[0].menu.descripcion == menu_usuario_model_create.menu.descripcion
    assert menus[0].menu.entrada == menu_usuario_model_create.menu.entrada
    assert menus[0].menu.ensalada == menu_usuario_model_create.menu.ensalada
    assert menus[0].menu.plato_fondo == menu_usuario_model_create.menu.plato_fondo
    assert menus[0].menu.postre == menu_usuario_model_create.menu.postre
    assert menus[0].menu.fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_model_create.menu.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].menu.usuario_creacion_id == menu_usuario_model_create.menu.usuario_creacion.id
    assert menus[0].menu.fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_model_create.menu.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].menu.status_id == menu_usuario_model_create.menu.status.id
    assert menus[0].menu.orden == menu_usuario_model_create.menu.orden

@pytest.mark.usefixtures('transactional_db')
def test_saves_usuario_menus_changes(menu_usuario_model_create: UsuarioMenuModel) -> None:
    usuario_created = UsuarioModel.objects.create(
        rut = '11.111.111-1', nombre = 'test', email = 'test@test.cl', fecha_registro = date.today(), 
        uid = 'qwertyqw', perfil = menu_usuario_model_create.usuario.perfil, password = 'test'
    )
    usuario_menu = UsuarioMenu(id = None, usuario_id = usuario_created.id, menu_id = menu_usuario_model_create.menu.id, observacion= 'TEST', fecha_registro = date.today())

    usuario_menu_save = DjangoORMUsuarioMenusRepository().save(usuario_menu)
    assert usuario_menu_save.usuario_id == usuario_created.id
    assert usuario_menu_save.menu_id == menu_usuario_model_create.menu.id
