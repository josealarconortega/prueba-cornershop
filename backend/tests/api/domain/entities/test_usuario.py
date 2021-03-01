import typing

from api.domain.entities import (
    Usuario
)


def create_usuario() -> Usuario:
    return Usuario(id =  1, nombre =  'test', rut =  '11.111.111-1', email =  'test@test.cl', fecha_registro =  '2021-01-01', uid =  'wqer', perfil_id =  1, perfil_descripcion = 'Mantencion', password =  'test')


def test_all_attributos():
    usuario = create_usuario()

    assert usuario.id == 1
    assert usuario.nombre == 'test'
    assert usuario.rut == '11.111.111-1'
    assert usuario.email == 'test@test.cl'
    assert usuario.fecha_registro == '2021-01-01'
    assert usuario.uid == 'wqer'
    assert usuario.perfil_id == 1
    assert usuario.password == 'test'
    assert str(usuario) == '<Usuario #1>'

