from decimal import Decimal
from unittest.mock import Mock, PropertyMock

import inject
import pytest
from django.test import Client

from api.apps import inject_config
from api.models import (
    Usuario as UsuarioModel,
    Perfil as PerfilModel,
    Menu as MenuModel,
    Status as StatusModel,
    UsuarioMenu as UsuarioMenuModel
)
from datetime import date, datetime
import hashlib 
from unittest.mock import Mock, PropertyMock
from api.application.ports import SlackGateway
from api.application.repositories import MenusRepository
from api.domain.entities import Menu

@pytest.fixture()
def exemplary_menu_id() -> int:
    return 1

@pytest.fixture()
def password():
    return 'test3'

@pytest.fixture()
def uid():
    return 'qwertyqw'

@pytest.fixture()
def status_registrado_with() -> StatusModel:
    status_created = StatusModel.objects.create(descripcion = 'Registrado')
    return status_created

@pytest.fixture()
def status_confirmado_with() -> StatusModel:
    status_created = StatusModel.objects.create(descripcion = 'Confirmado')
    return status_created

@pytest.fixture()
def perfil_empleado_with() -> PerfilModel:
    perfil_empleado = PerfilModel.objects.create(descripcion = 'Empleado')
    return perfil_empleado

@pytest.fixture()
def perfil_mantencion_with() -> PerfilModel:
    perfil_mantencion = PerfilModel.objects.create(descripcion = 'Mantencion')
    return perfil_mantencion

@pytest.fixture()
def menu(exemplary_menu_id: int) -> Menu:
    return Menu(id = exemplary_menu_id, descripcion = 'test', entrada = 'entrada',  
                ensalada = 'ensalada', plato_fondo = 'plato_fondo', postre = 'postre',
                fecha_registro = 'fecha_registro', usuario_creacion_id = 1, 
                fecha_menu = '2021-01-01', status_id = 1, status_descripcion = "Mantencion", orden = 1)

@pytest.fixture()
def usuario_with(password: str, uid: str, perfil_mantencion_with: PerfilModel) -> UsuarioModel:
    usuario_created = UsuarioModel.objects.create(
        rut = '33.333.333-3', nombre = 'test', email = 'test@test.cl', fecha_registro = date.today(), 
        uid = uid, perfil = perfil_mantencion_with, password = hashlib.md5(password.encode()).hexdigest()
    )
    return usuario_created

@pytest.fixture()
def usuario_empleado_with(password: str, uid: str, perfil_empleado_with: PerfilModel) -> UsuarioModel:
    usuario_created = UsuarioModel.objects.create(
        rut = '44.444.444-4', nombre = 'test', email = 'test3@test3.cl', fecha_registro = date.today(), 
        uid = uid, perfil = perfil_empleado_with, password = hashlib.md5(password.encode()).hexdigest()
    )
    return usuario_created

@pytest.fixture()
def menu_with(usuario_with: UsuarioModel, status_registrado_with: StatusModel) -> MenuModel:
    menu_created = MenuModel.objects.create(
        descripcion = 'Menu', entrada = 'entrada', ensalada = 'ensalada', plato_fondo = 'plato', 
        postre = 'postre', fecha_registro = date.today(), usuario_creacion = usuario_with, 
        fecha_menu = date.today(), status = status_registrado_with, orden = 1)
    return menu_created

@pytest.fixture()
def menu_confirmation_with(usuario_with: UsuarioModel, status_confirmado_with: StatusModel) -> MenuModel:
    menu_created = MenuModel.objects.create(
        descripcion = 'Menu', entrada = 'entrada', ensalada = 'ensalada', plato_fondo = 'plato', 
        postre = 'postre', fecha_registro = date.today(), usuario_creacion = usuario_with, 
        fecha_menu = date.today(), status = status_confirmado_with, orden = 1)
    return menu_created

@pytest.fixture()
def usuario_menu_with(usuario_empleado_with: UsuarioModel, menu_confirmation_with: MenuModel) -> UsuarioMenuModel:
    usuario_menu_created = UsuarioMenuModel.objects.create(
        usuario = usuario_empleado_with, menu = menu_confirmation_with, observacion = "Test", fecha_registro = date.today()
    )
    return usuario_menu_created

@pytest.fixture()
def slack_gateway_adapters_mock() -> Mock:
    return Mock(spec_set=SlackGateway, notify_user=Mock(return_value=True))

@pytest.fixture()
def menu_repo_mock(menu: Menu) -> Mock:
    return Mock(spec_set=MenusRepository, get_by_id=Mock(return_value=menu), save = Mock(return_value=menu), get_by_id_list =  Mock(return_value=[menu]), get_by_date = Mock(return_value=[menu]))

@pytest.fixture(autouse=True)
def dependency_injection_config(
    menu_repo_mock: Mock
) -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(MenusRepository, menu_repo_mock)
    inject.clear_and_configure(inject_config)
