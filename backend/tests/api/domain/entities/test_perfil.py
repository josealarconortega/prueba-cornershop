import typing

from api.domain.entities import (
    Perfil
)


def create_perfil() -> Perfil:
    return Perfil(id = 1, descripcion = 'test')


def test_all_attributos():
    perfil = create_perfil()

    assert perfil.id == 1
    assert perfil.descripcion == 'test'
