from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model

from api.infrastructure.repositories import DjangoORMUsuariosRepository
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
    Perfil as PerfilModel,
    UsuarioMenu as UsuarioMenuModel
)

from datetime import date, datetime

@pytest.fixture()
def usuario_model_create() -> UsuarioModel:
    perfil_mantencion = PerfilModel.objects.create(descripcion = 'Mantencion')
    perfil_empleado = PerfilModel.objects.create(descripcion = 'Usuario')
    status = StatusModel.objects.create(descripcion = 'Registrado')
    usuario_created = UsuarioModel.objects.create(
        rut = '11.111.111-1', nombre = 'test', email = 'test@test.cl', fecha_registro = date.today(), 
        uid = 'qwertyqw', perfil = perfil_mantencion, password = 'test'
    )
    return usuario_created


@pytest.mark.usefixtures('transactional_db')
def test_gets_by_id_user(usuario_model_create: UsuarioMenuModel) -> None:
    usuario = DjangoORMUsuariosRepository().get_by_id(usuario_model_create.id)
    assert usuario.id == usuario_model_create.id
    assert usuario.rut == usuario_model_create.rut
    assert usuario.nombre == usuario_model_create.nombre
    assert usuario.email == usuario_model_create.email
    assert usuario.fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuario.uid == usuario_model_create.uid
    assert usuario.perfil_id== usuario_model_create.perfil.id
    assert usuario.password == usuario_model_create.password

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_all(usuario_model_create: UsuarioMenuModel) -> None:
    usuarios = DjangoORMUsuariosRepository().get_all()
    assert usuarios[0].id == usuario_model_create.id
    assert usuarios[0].rut == usuario_model_create.rut
    assert usuarios[0].nombre == usuario_model_create.nombre
    assert usuarios[0].email == usuario_model_create.email
    assert usuarios[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuarios[0].uid == usuario_model_create.uid
    assert usuarios[0].perfil_id== usuario_model_create.perfil.id
    assert usuarios[0].password == usuario_model_create.password

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_all_by_perfil(usuario_model_create: UsuarioMenuModel) -> None:
    usuarios = DjangoORMUsuariosRepository().get_all_by_perfil(usuario_model_create.perfil.id)
    assert usuarios[0].id == usuario_model_create.id
    assert usuarios[0].rut == usuario_model_create.rut
    assert usuarios[0].nombre == usuario_model_create.nombre
    assert usuarios[0].email == usuario_model_create.email
    assert usuarios[0].fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuarios[0].uid == usuario_model_create.uid
    assert usuarios[0].perfil_id== usuario_model_create.perfil.id
    assert usuarios[0].password == usuario_model_create.password

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_by_uid(usuario_model_create: UsuarioMenuModel) -> None:
    usuario = DjangoORMUsuariosRepository().get_by_uid(usuario_model_create.uid)
    assert usuario.id == usuario_model_create.id
    assert usuario.rut == usuario_model_create.rut
    assert usuario.nombre == usuario_model_create.nombre
    assert usuario.email == usuario_model_create.email
    assert usuario.fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuario.uid == usuario_model_create.uid
    assert usuario.perfil_id== usuario_model_create.perfil.id
    assert usuario.password == usuario_model_create.password

@pytest.mark.usefixtures('transactional_db')
def test_gets_by_by_user_pass(usuario_model_create: UsuarioMenuModel) -> None:
    usuario = DjangoORMUsuariosRepository().get_user_password(usuario_model_create.rut, usuario_model_create.password)
    assert usuario.id == usuario_model_create.id
    assert usuario.rut == usuario_model_create.rut
    assert usuario.nombre == usuario_model_create.nombre
    assert usuario.email == usuario_model_create.email
    assert usuario.fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_model_create.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuario.uid == usuario_model_create.uid
    assert usuario.perfil_id== usuario_model_create.perfil.id
    assert usuario.password == usuario_model_create.password

@pytest.mark.usefixtures('transactional_db')
def test_saves_usuario(usuario_model_create: UsuarioMenuModel) -> None:
    usuario_created = Usuario(
        id = None, rut = '11.111.111-1', nombre = 'test', email = 'test@test.cl', fecha_registro = date.today(), 
        uid = 'qwertyqw', perfil_id = usuario_model_create.perfil.id, password = 'test'
    )
    usuario_save = DjangoORMUsuariosRepository().save(usuario_created)
    assert usuario_save.rut == usuario_created.rut
    assert usuario_save.nombre == usuario_created.nombre
    assert usuario_save.email == usuario_created.email
    assert usuario_save.fecha_registro.strftime("%Y%M%D %H:%M:%S") == usuario_created.fecha_registro.strftime("%Y%M%D %H:%M:%S")
    assert usuario_save.uid == usuario_created.uid
    assert usuario_save.perfil_id== usuario_created.perfil_id
    assert usuario_save.password == usuario_created.password



