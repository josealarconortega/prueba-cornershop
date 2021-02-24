from decimal import Decimal

import inject
import pytest
from django.test import Client

from api.apps import inject_config
from api.models import (
    Usuario as UsuarioModel,
    Perfil as PerfilModel
)
from datetime import date, datetime
import hashlib 

@pytest.fixture()
def password():
    return 'test3'

@pytest.fixture()
def uid():
    return 'qwertyqw'

@pytest.fixture()
def usuario_with(password: str, uid: str) -> UsuarioModel:
    perfil_mantencion = PerfilModel.objects.create(descripcion = 'Mantencion')
    usuario_created = UsuarioModel.objects.create(
        rut = '33.333.333-3', nombre = 'test', email = 'test3@test3.cl', fecha_registro = date.today(), 
        uid = uid, perfil = perfil_mantencion, password = hashlib.md5(password.encode()).hexdigest()
    )
    return usuario_created

@pytest.fixture(autouse=True)
def dependency_injection_config() -> None:
    inject.clear_and_configure(inject_config)
