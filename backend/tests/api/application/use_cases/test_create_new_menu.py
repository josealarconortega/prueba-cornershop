from unittest.mock import (
    Mock,
    patch,
)

import pytest

from api.application.use_cases import MakeNewMenuUseCase
from api.application.use_cases.create_new_menu import MenuInputDto, MenuMakeOutputDto, MenuDescripcionDTO
from api.domain.entities import (
    Menu, Usuario
) 
import typing
from datetime import date, datetime
from api.application.repositories import MenusRepository, UsuariosRepository


@pytest.fixture()
def usuario_id() -> int:
    return 1

@pytest.fixture()
def descripcion() -> str:
    return 'menu prueba'

@pytest.fixture()
def entrada() -> str:
    return 'entrada prueba'

@pytest.fixture()
def ensalada() -> str:
    return 'ensalada prueba'

@pytest.fixture()
def plato_fondo() -> str:
    return 'plato_fondo prueba'

@pytest.fixture()
def postre() -> str:
    return 'postre prueba'

@pytest.fixture()
def status_id() -> int:
    return 1

@pytest.fixture()
def fecha_menu() -> str:
    return '2021-02-01 00:00:00'

@pytest.fixture()
def orden() -> int:
    return 1

@pytest.fixture()
def descripcion_menu_dto(descripcion: str, entrada: str, ensalada: str, plato_fondo: str, postre: str, status_id: int, fecha_menu: str) -> MenuDescripcionDTO:
    return [MenuDescripcionDTO(descripcion, entrada, ensalada, plato_fondo, postre, status_id, fecha_menu)]

@pytest.fixture()
def input_dto(exemplary_usuario_id: int, descripcion_menu_dto: typing.List[MenuDescripcionDTO]) -> MenuInputDto:
    return MenuInputDto(exemplary_usuario_id, descripcion_menu_dto)

def test_loads_user_using_id_found(
        exemplary_usuario_id: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    MakeNewMenuUseCase().execute(input_dto)
    usuario_repo_mock.get_by_id.assert_called_once_with(exemplary_usuario_id)

def test_loads_user_using_id_not_found(
        exemplary_usuario_id: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    usuario_repo_mock.get_by_id.return_value = None
    MakeNewMenuUseCase().execute(input_dto)
    usuario_repo_mock.get_by_id.assert_called_once_with(exemplary_usuario_id)


