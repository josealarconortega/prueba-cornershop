from unittest.mock import (
    Mock,
    patch,
)

import pytest

from api.application.use_cases import UpdateUserUseCase
from api.application.use_cases.update_new_user import MenuInputDto, UserMakeOutputDto
from api.domain.entities import (
    Menu, Usuario
) 
import typing
from datetime import date, datetime
from api.application.repositories import MenusRepository, UsuariosRepository


@pytest.fixture()
def rut() -> str:
    return '11.111.111-1'

@pytest.fixture()
def nombre() -> str:
    return 'nombre'

@pytest.fixture()
def email() -> str:
    return 'test@test.cl'

@pytest.fixture()
def perfil_id() -> int:
    return 1

@pytest.fixture()
def password() -> str:
    return 'qwerty'


@pytest.fixture()
def input_dto(exemplary_usuario_id: int, rut: rut, nombre: nombre, email: email, exemplary_perfil_id: int, password = password) -> MenuInputDto:
    return MenuInputDto(exemplary_usuario_id, rut, nombre, email, exemplary_perfil_id, password)

def test_loads_perfil_using_id_found(
        exemplary_perfil_id: int,
        perfil_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    UpdateUserUseCase().execute(input_dto)
    perfil_repo_mock.get_by_id.assert_called_once_with(exemplary_perfil_id)

def test_loads_user_using_id_not_found(
        exemplary_perfil_id: int,
        perfil_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    perfil_repo_mock.get_by_id.return_value = None
    UpdateUserUseCase().execute(input_dto)
    perfil_repo_mock.get_by_id.assert_called_once_with(exemplary_perfil_id)