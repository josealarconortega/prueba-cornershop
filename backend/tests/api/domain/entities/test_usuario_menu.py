import typing

from api.domain.entities import (
    UsuarioMenu
)


def create_usuario_menu() -> UsuarioMenu:
    return UsuarioMenu(id =  1, usuario_id= 1, menu_id= 1, observacion='test', fecha_registro='2021-01-01')


def test_all_attributos():
    usuario_menu = create_usuario_menu()

    assert usuario_menu.id == 1
    assert usuario_menu.usuario_id == 1
    assert usuario_menu.menu_id == 1
    assert usuario_menu.observacion == 'test'
    assert usuario_menu.fecha_registro == '2021-01-01'

