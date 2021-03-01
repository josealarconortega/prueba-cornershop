from unittest.mock import (
    Mock,
    patch,
)

import pytest

from api.application.use_cases import MakeAnOrderUseCase
from api.application.use_cases.make_an_order import MenuInputDto, MenuMakeOutputDto
from api.domain.entities import (
    Menu, Usuario
) 
import typing
from datetime import date, datetime
from api.application.repositories import MenusRepository, UsuariosRepository

@pytest.fixture()
def menu_usuario_id() -> int:
    return 1

@pytest.fixture()
def usuario_id() -> int:
    return 1

@pytest.fixture()
def menu_id() -> int:
    return 1

@pytest.fixture()
def descripcion() -> str:
    return 'sin palta'


@pytest.fixture()
def input_dto(exemplary_usuario_id: int, exemplary_menu_id: int, descripcion: str) -> MenuInputDto:
    return MenuInputDto(exemplary_usuario_id, exemplary_menu_id, descripcion)

def test_loads_menu_using_id_found(
        exemplary_menu_id: int,
        menu_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    MakeAnOrderUseCase().execute(input_dto)
    menu_repo_mock.get_by_id.assert_called_once_with(exemplary_menu_id)

def test_loads_menu_using_id_not_found(
        exemplary_menu_id: int,
        menu_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    menu_repo_mock.get_by_id.return_value = None
    MakeAnOrderUseCase().execute(input_dto)
    menu_repo_mock.get_by_id.assert_called_once_with(exemplary_menu_id)


def test_loads_user_using_id_found(
        exemplary_usuario_id: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    MakeAnOrderUseCase().execute(input_dto)
    usuario_repo_mock.get_by_id.assert_called_once_with(exemplary_usuario_id)

def test_loads_user_using_id_not_found(
        exemplary_menu_id: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    usuario_repo_mock.get_by_id.return_value = None
    MakeAnOrderUseCase().execute(input_dto)
    usuario_repo_mock.get_by_id.assert_called_once_with(exemplary_menu_id)


