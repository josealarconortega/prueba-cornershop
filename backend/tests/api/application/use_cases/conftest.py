from decimal import Decimal
from unittest.mock import Mock, PropertyMock

import inject
import pytest

from api.application.repositories import MenusRepository, UsuariosRepository, PerfilRepository, UsuarioMenusRepository
from api.application.ports import SlackGateway
from api.domain.entities import Menu, Usuario, Perfil, UsuarioMenu


@pytest.fixture()
def exemplary_menu_id() -> int:
    return 1

@pytest.fixture()
def exemplary_usuario_menu_id() -> int:
    return 1

@pytest.fixture()
def exemplary_usuario_ids() -> int:
    return [1, 2, 3]

@pytest.fixture()
def exemplary_usuario_id() -> int:
    return 1

@pytest.fixture()
def exemplary_perfil_id() -> int:
    return 1

@pytest.fixture()
def menu(exemplary_menu_id: int) -> Menu:
    return Menu(id = exemplary_menu_id, descripcion = 'test', entrada = 'entrada',  
                ensalada = 'ensalada', plato_fondo = 'plato_fondo', postre = 'postre',
                fecha_registro = 'fecha_registro', usuario_creacion_id = 1, 
                fecha_menu = '2021-01-01', status_id = 1, orden = 'orden')

@pytest.fixture()
def usuario(exemplary_usuario_id: int) -> Usuario:
    return Usuario(id = exemplary_usuario_id,rut = '11.111.111-1', nombre = 'nombre', 
                email = 'email@test.cl', fecha_registro = '2021-03-10', uid = 'wqeryure', 
                perfil_id = 1, password = 'qwe')

@pytest.fixture()
def perfil(exemplary_perfil_id: int) -> Perfil:
    return Perfil(id = exemplary_perfil_id, descripcion = 'Perfil pruebas')

@pytest.fixture()
def usuario_menu(exemplary_usuario_menu_id: int) -> Perfil:
    return UsuarioMenu(id = exemplary_usuario_menu_id, usuario_id = 1, menu_id = 1,observacion = 'sin palta',fecha_registro = '2021-01-01' )


@pytest.fixture()
def menu_repo_mock(menu: Menu) -> Mock:
    return Mock(spec_set=MenusRepository, get_by_id=Mock(return_value=menu), save = Mock(return_value=menu))

@pytest.fixture()
def usuario_repo_mock(usuario: Usuario) -> Mock:
    return Mock(spec_set=UsuariosRepository, get_by_id=Mock(return_value=usuario))

@pytest.fixture()
def perfil_repo_mock(perfil: Perfil) -> Mock:
    return Mock(spec_set=PerfilRepository, get_by_id=Mock(return_value=perfil))

@pytest.fixture()
def usuario_menu_repo_mock(usuario_menu: UsuarioMenu) -> Mock:
    return Mock(spec_set=UsuarioMenusRepository, save=Mock(return_value=usuario_menu))

@pytest.fixture()
def slack_gateway_adapters_mock() -> Mock:
    return Mock(spec_set=SlackGateway)


@pytest.fixture(autouse=True)
def dependency_injection_config(
    menu_repo_mock: Mock,
    usuario_repo_mock: Mock,
    perfil_repo_mock: Mock,
    usuario_menu_repo_mock: Mock,
    slack_gateway_adapters_mock: Mock
) -> None:
    def configure(binder: inject.Binder) -> None:
        binder.bind(MenusRepository, menu_repo_mock)
        binder.bind(UsuariosRepository, usuario_repo_mock )
        binder.bind(PerfilRepository, perfil_repo_mock )
        binder.bind(UsuarioMenusRepository, usuario_menu_repo_mock)
        binder.bind(SlackGateway, slack_gateway_adapters_mock)
    inject.clear_and_configure(configure)
