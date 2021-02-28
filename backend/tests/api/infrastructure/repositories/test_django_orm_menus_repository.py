from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from api.infrastructure.repositories import DjangoORMMenusRepository
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
    Perfil as PerfilModel
)

from datetime import date, datetime

@pytest.fixture()
def menu_usuario_menu_model_create() -> MenuModel:
    perfil = PerfilModel.objects.create(descripcion = 'Mantencion')
    status = StatusModel.objects.create(descripcion = 'Registrado')
    usuario = UsuarioModel.objects.create(
        rut = '11.111.111-1',
        nombre = 'test',
        email = 'test@test.cl',
        fecha_registro = date.today(),
        uid = 'qwertyqw',
        perfil = perfil,
        password = 'test'
    )
    menu = MenuModel.objects.create(
        descripcion = 'Menu',
        entrada = 'entrada',
        ensalada = 'ensalada',
        plato_fondo = 'plato',
        postre = 'postre',
        fecha_registro = date.today(),
        usuario_creacion = usuario,
        fecha_menu = date.today(),
        status = status,
        orden = 1
    )
    
    return menu


@pytest.mark.usefixtures('transactional_db')
def test_gets_all_existing_menu(menu_usuario_menu_model_create: MenuModel) -> None:
    menus = DjangoORMMenusRepository().get_all()
    assert menus[0].id == menu_usuario_menu_model_create.id
    assert menus[0].descripcion == menu_usuario_menu_model_create.descripcion
    assert menus[0].entrada == menu_usuario_menu_model_create.entrada
    assert menus[0].ensalada == menu_usuario_menu_model_create.ensalada
    assert menus[0].plato_fondo == menu_usuario_menu_model_create.plato_fondo
    assert menus[0].postre == menu_usuario_menu_model_create.postre
    assert menus[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].usuario_creacion_id == menu_usuario_menu_model_create.usuario_creacion.id
    assert menus[0].fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].status_id == menu_usuario_menu_model_create.status.id
    assert menus[0].orden == menu_usuario_menu_model_create.orden

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_id_existing_menu(menu_usuario_menu_model_create: MenuModel) -> None:
    menu = DjangoORMMenusRepository().get_by_id(menu_usuario_menu_model_create.id)
    assert menu.id == menu_usuario_menu_model_create.id
    assert menu.descripcion == menu_usuario_menu_model_create.descripcion
    assert menu.entrada == menu_usuario_menu_model_create.entrada
    assert menu.ensalada == menu_usuario_menu_model_create.ensalada
    assert menu.plato_fondo == menu_usuario_menu_model_create.plato_fondo
    assert menu.postre == menu_usuario_menu_model_create.postre
    assert menu.fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menu.usuario_creacion_id == menu_usuario_menu_model_create.usuario_creacion.id
    assert menu.fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menu.status_id == menu_usuario_menu_model_create.status.id
    assert menu.orden == menu_usuario_menu_model_create.orden

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_id_list_existing_menu(menu_usuario_menu_model_create: MenuModel) -> None:
    id = menu_usuario_menu_model_create.id
    menus = DjangoORMMenusRepository().get_by_id_list([id])
    assert menus[0].id == menu_usuario_menu_model_create.id
    assert menus[0].descripcion == menu_usuario_menu_model_create.descripcion
    assert menus[0].entrada == menu_usuario_menu_model_create.entrada
    assert menus[0].ensalada == menu_usuario_menu_model_create.ensalada
    assert menus[0].plato_fondo == menu_usuario_menu_model_create.plato_fondo
    assert menus[0].postre == menu_usuario_menu_model_create.postre
    assert menus[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].usuario_creacion_id == menu_usuario_menu_model_create.usuario_creacion.id
    assert menus[0].fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].status_id == menu_usuario_menu_model_create.status.id
    assert menus[0].orden == menu_usuario_menu_model_create.orden

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_date_existing_menu(menu_usuario_menu_model_create: MenuModel) -> None:
    menus = DjangoORMMenusRepository().get_by_date(menu_usuario_menu_model_create.fecha_registro )
    assert menus[0].id == menu_usuario_menu_model_create.id
    assert menus[0].descripcion == menu_usuario_menu_model_create.descripcion
    assert menus[0].entrada == menu_usuario_menu_model_create.entrada
    assert menus[0].ensalada == menu_usuario_menu_model_create.ensalada
    assert menus[0].plato_fondo == menu_usuario_menu_model_create.plato_fondo
    assert menus[0].postre == menu_usuario_menu_model_create.postre
    assert menus[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].usuario_creacion_id == menu_usuario_menu_model_create.usuario_creacion.id
    assert menus[0].fecha_menu.strftime("%Y%M%D %H:%M:%S") == menu_usuario_menu_model_create.fecha_menu.strftime("%Y%M%D %H:%M:%S")
    assert menus[0].status_id == menu_usuario_menu_model_create.status.id
    assert menus[0].orden == menu_usuario_menu_model_create.orden

@pytest.mark.usefixtures('transactional_db')
def test_updates_menu(menu_usuario_menu_model_create: MenuModel) -> None:
    status_confirmation = StatusModel.objects.create(descripcion = 'Confirmado')
    id = menu_usuario_menu_model_create.id
    menu = DjangoORMMenusRepository().get_by_id(id)
    menu.setStatus(status_confirmation.id)
    menu_update = DjangoORMMenusRepository().update(menu)
    #menu = DjangoORMMenusRepository().update(menu)
    assert menu_update.status_id == menu.status_id


@pytest.mark.usefixtures('transactional_db')
def test_saves_menu_changes(menu_usuario_menu_model_create: MenuModel) -> None:
    menu = Menu(id = None, descripcion = 'test', entrada = 'entrada',  
                ensalada = 'ensalada', plato_fondo = 'plato_fondo', postre = 'postre',
                fecha_registro = '2021-01-01', usuario_creacion_id = menu_usuario_menu_model_create.usuario_creacion.id , 
                fecha_menu = '2021-01-01', status_id = menu_usuario_menu_model_create.status.id, status_descripcion= menu_usuario_menu_model_create.status.descripcion, orden = 0)

    menu_save = DjangoORMMenusRepository().save(menu)

    assert menu_save.status_id == menu_usuario_menu_model_create.status.id
    assert menu_save.usuario_creacion_id == menu_usuario_menu_model_create.usuario_creacion.id

