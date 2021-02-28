import json

import dacite
from django.http import (
    HttpRequest,
    HttpResponse
)

from api.application import (
    repositories
)
from api.application.use_cases import make_an_order, make_confirmation_menu, create_new_menu, create_new_user, update_new_user, update_new_menu
from rest_framework.decorators import api_view,permission_classes
from config.decorators import serialize_exceptions
from api.serializers import UsuarioMenuSerializer, UsuarioSerializer, MultipleUsuarioSerializer, MultipleMenuSerializer, MultipleUsuarioMenuSerializer, PerfilSerializer, MultiplePerfilSerializer
from api.domain.value_objects import Response
import hashlib 
import os
from django.conf import settings
import inject
from datetime import datetime

@api_view(['POST'])
@serialize_exceptions
def login_required(request: HttpRequest) -> HttpResponse:
    data_dto = json.loads(request.body)
    repo: repositories.UsuariosRepository = inject.instance(repositories.UsuariosRepository)
    usuario = repo.get_user_password(rut = data_dto['rut'], password = hashlib.md5(data_dto['password'].encode()).hexdigest(), perfil_id = data_dto['perfil_id'])
    code = 0
    status = 400
    message = 'Error'
    data = None
    if usuario is None:
        message = 'Credenciales incorrectas'
        status = 500
    else:
        message = 'Ingresado correctamente'
        status = 200
        code = 1
        data = UsuarioSerializer.serialize(usuario)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['GET'])
@serialize_exceptions
def user_by_uid(request: HttpRequest, uid: str) -> HttpResponse:
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.UsuariosRepository = inject.instance(repositories.UsuariosRepository)
    usuario = repo.get_by_uid(uid)
    if usuario is None:
        message = 'Usuario no encontrado'
        status = 500
    else:
        message = 'Usuario encontrado'
        status = 200
        code = 1
        data = UsuarioSerializer.serialize(usuario)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')
@api_view(['POST'])
@serialize_exceptions
def create_user(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    password = hashlib.md5(data['password'].encode()).hexdigest()
    input_dto = dacite.from_dict(create_new_user.MenuInputDto, {
        'rut': data['rut'],
        'nombre': data['nombre'],
        'email': data['email'],
        'perfil_id': data['perfil_id'],
        'password': password
    })
    uc = create_new_user.MakeNewUserUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = (UsuarioSerializer.serialize(output_dto.data) if output_dto.data is not None else None)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['POST'])
@serialize_exceptions
def menu_by_date(request: HttpRequest) -> HttpResponse:
    data_dto = json.loads(request.body)
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.MenusRepository = inject.instance(repositories.MenusRepository)
    menus = repo.get_by_date(datetime.strptime(str(data_dto['fecha']), '%Y-%m-%d %H:%M:%S'))
    if menus is None:
        message = 'Error al obtener el menu'
        status = 500
    else:
        message = 'Menus encontrados'
        status = 200
        code = 1
        data = MultipleMenuSerializer.serialize(menus)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['POST'])
@serialize_exceptions
def menu_by_date_status(request: HttpRequest) -> HttpResponse:
    data_dto = json.loads(request.body)
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.MenusRepository = inject.instance(repositories.MenusRepository)
    menus = repo.get_by_date_status(datetime.strptime(str(data_dto['fecha']), '%Y-%m-%d %H:%M:%S'), data_dto['status'])
    if menus is None:
        message = 'Error al obtener el menu'
        status = 500
    else:
        message = 'Menus encontrados'
        status = 200
        code = 1
        data = MultipleMenuSerializer.serialize(menus)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['POST'])
def create_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(create_new_menu.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menus': data['menus']
    })
    uc = create_new_menu.MakeNewMenuUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = MultipleMenuSerializer.serialize(output_dto.data)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['DELETE'])
def eliminar_menu(request: HttpRequest, menu_id: int) -> HttpResponse:
    repo: repositories.MenusRepository = inject.instance(repositories.MenusRepository)
    menu = repo.get_by_id(menu_id)
    code = 0
    status = 400
    message = 'Error'
    data = None
    if menu.status_id == settings.STATUS_CONFIRMATION:
        status = 400
        message = 'Menu ya fue enviado y no se puede eliminar'
    else:
        delete_menu = repo.delete(menu_id)
        if delete_menu:
            message = 'Eliminado correctamente'
            status = 200
            code = 1
        else:
            message = 'Error al eliminar el menu'
            status = 500
    data = Response(code = code, status = status, message= message, data = None).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')
@api_view(['POST'])
def editar_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(update_new_menu.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menus': data['menus']
    })
    uc = update_new_menu.UpdateMenuUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = MultipleMenuSerializer.serialize(output_dto.data)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')
    
@api_view(['POST'])
@serialize_exceptions
def confirmation_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(make_confirmation_menu.MenuInputDto, {
        'perfil_id': data['perfil_id'],
        'menu_ids': data['menu_ids'],
        'status_id': data['status_id']
    })

    uc = make_confirmation_menu.ConfirmationUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = None).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['POST'])
@serialize_exceptions
def select_menu_usuario(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(make_an_order.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menu_id': data['menu_id'],
        'observacion': data['observacion']
    })

    uc = make_an_order.MakeAnOrderUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = (UsuarioMenuSerializer.serialize(output_dto.data) if output_dto.data is not None else None)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['GET'])
def obtener_perfiles(request: HttpRequest) -> HttpResponse:
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.PerfilRepository = inject.instance(repositories.PerfilRepository)
    perfiles = repo.get_all()
    if perfiles is None:
        message = 'Error al obtener perfiles'
        status = 500
    else:
        message = 'Perfiles encontrados'
        status = 200
        code = 1
        data = MultiplePerfilSerializer.serialize(perfiles)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['GET'])
def obtener_usuarios(request: HttpRequest) -> HttpResponse:
    code = 0
    status = 400
    message = 'Error'
    data = None 
    repo: repositories.UsuariosRepository = inject.instance(repositories.UsuariosRepository)
    usuarios = repo.get_all()
    if usuarios is None:
        message = 'Usuarios no encontrado'
        status = 500
    else:
        message = 'Usuario encontrado'
        status = 200
        code = 1
        data = MultipleUsuarioSerializer.serialize(usuarios)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['POST'])
def editar_usuario(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    password = hashlib.md5(data['password'].encode()).hexdigest()
    input_dto = dacite.from_dict(update_new_user.MenuInputDto, {
        'usuario_id': data['usuario_id'],
        'rut': data['rut'],
        'nombre': data['nombre'],
        'email': data['email'],
        'perfil_id': data['perfil_id'],
        'password': password,
    })
    uc = update_new_user.MakeNewUserUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = (UsuarioSerializer.serialize(output_dto.data) if output_dto.data is not None else None)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['DELETE'])
def eliminar_usuario(request: HttpRequest, usuario_id: int) -> HttpResponse:
    repo: repositories.UsuariosRepository = inject.instance(repositories.UsuariosRepository)
    usuario = repo.get_by_id(usuario_id)
    code = 0
    status = 400
    message = 'Error'
    data = None
    delete_usuario = repo.delete(usuario_id)
    if delete_usuario:
        message = 'Eliminado correctamente'
        status = 200
        code = 1
    else:
        message = 'Error al eliminar el usuario'
        status = 500
    data = Response(code = code, status = status, message= message, data = None).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')


@api_view(['POST'])
def obtener_menus_usuario_id_fecha(request: HttpRequest, usuario_id: int) -> HttpResponse:
    data_dto = json.loads(request.body)
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.UsuarioMenusRepository = inject.instance(repositories.UsuarioMenusRepository)
    menus = repo.get_menu_by_usuario_id(usuario_id, datetime.strptime(str(data_dto['fecha_menu']), '%Y-%m-%d %H:%M:%S'))
    if menus is None:
        message = 'Error al obtener usuarios'
        status = 500
    else:
        message = 'Usuarios encontrados'
        status = 200
        code = 1
        data = MultipleMenuSerializer.serialize(menus)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

@api_view(['POST'])
def obtener_menus_usuario_fecha(request: HttpRequest) -> HttpResponse:
    data_dto = json.loads(request.body)
    code = 0
    status = 400
    message = 'Error'
    data = None
    repo: repositories.UsuarioMenusRepository = inject.instance(repositories.UsuarioMenusRepository)
    usuarioMenus = repo.get_menu_usuario_by_fecha( datetime.strptime(str(data_dto['fecha_menu']), '%Y-%m-%d %H:%M:%S'))
    if usuarioMenus is None:
        message = 'Error al obtener los registros'
        status = 500
    else:
        message = 'Datos encontrados'
        status = 200
        code = 1
        data = MultipleUsuarioMenuSerializer.serialize(usuarioMenus)
    data = Response(code = code, status = status, message= message, data = data).toResponse()
    return HttpResponse(data, status=status, content_type='application/json')

