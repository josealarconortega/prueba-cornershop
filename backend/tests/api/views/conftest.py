from decimal import Decimal

import inject
import pytest
from django.test import Client

from api.apps import inject_config
from api.models import (
    Usuario as UsuarioModel,
    Perfil as PerfilModel,
    Menu as MenuModel,
    Status as StatusModel
)
from datetime import date, datetime
import hashlib 
from unittest.mock import Mock, PropertyMock
from api.application.ports import SlackGateway

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
def slack_gateway_adapters_mock() -> Mock:
    return Mock(spec_set=SlackGateway, notify_user=Mock(return_value=True))

@pytest.fixture(autouse=True)
def dependency_injection_config() -> None:
    inject.clear_and_configure(inject_config)
