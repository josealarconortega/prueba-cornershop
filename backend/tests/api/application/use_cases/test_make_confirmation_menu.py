from unittest.mock import (
    Mock,
    patch,
)

import pytest

from api.application.use_cases import ConfirmationUseCase
from api.application.use_cases.make_confirmation_menu import MenuInputDto, MenuMakeOutputDto
from api.domain.entities import (
    Menu, Usuario
) 
import typing
from datetime import date, datetime
from api.application.repositories import MenusRepository, UsuariosRepository

@pytest.fixture()
def menu_id() -> int:
    return 1

@pytest.fixture()
def usuario_id() -> int:
    return 1

@pytest.fixture()
def menu_ids() -> typing.List:
    return 1

@pytest.fixture()
def status_id() -> str:
    return 'sin palta'


@pytest.fixture()
def input_dto(exemplary_perfil_id_empleado: int, exemplary_menus_ids: [int], exemplary_status_id: int) -> MenuInputDto:
    return MenuInputDto(exemplary_perfil_id_empleado, exemplary_menus_ids, exemplary_status_id)

@pytest.mark.usefixtures('transactional_db')
def test_loads_user_using_id_found(
        exemplary_perfil_id_empleado: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    ConfirmationUseCase().execute(input_dto)
    usuario_repo_mock.get_all_by_perfil.assert_called_once_with(exemplary_perfil_id_empleado)

@pytest.mark.usefixtures('transactional_db')
def test_loads_user_using_id_not_found(
        exemplary_perfil_id_empleado: int,
        usuario_repo_mock: Mock,
        input_dto: input_dto
) -> None:
    usuario_repo_mock.get_all_by_perfil.return_value = None
    ConfirmationUseCase().execute(input_dto)
    usuario_repo_mock.get_all_by_perfil.assert_called_once_with(exemplary_perfil_id_empleado)

@pytest.mark.usefixtures('transactional_db')
def test_loads_user_using_slack_found(
        exemplary_perfil_id_empleado: int,
        slack_gateway_adapters_mock: Mock,
        input_dto: input_dto
) -> None:
    slack_gateway_adapters_mock.notify_user.return_value = True
    ConfirmationUseCase().execute(input_dto)
