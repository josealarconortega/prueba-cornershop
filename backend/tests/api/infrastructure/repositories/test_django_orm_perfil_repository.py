from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from api.infrastructure.repositories import DjangoORMPerfilRepository
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
def perfil_model_create() -> PerfilModel:
    perfil = PerfilModel.objects.create(descripcion = 'Mantencion')
    return perfil

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_id_existing_menu(perfil_model_create: PerfilModel) -> None:
    menu = DjangoORMPerfilRepository().get_by_id(perfil_model_create.id)
    assert menu.id == perfil_model_create.id
    assert menu.descripcion == perfil_model_create.descripcion