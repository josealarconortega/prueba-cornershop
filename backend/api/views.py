import json

import dacite
import inject
from django.http import (
    HttpRequest,
    HttpResponse
)

from api.application import (
    repositories
)
from api.application.use_cases import make_an_order, make_confirmation_menu, create_new_menu, create_new_user
from rest_framework.decorators import api_view,permission_classes
from config.decorators import serialize_exceptions
from api.serializers import UsuarioMenuSerializer, UsuarioSerializer, MultipleMenuSerializer
from api.domain.value_objects import Response
import hashlib 
import os


@api_view(['POST'])
@serialize_exceptions
def login_required(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    repo: repositories.UsuariosRepository = inject.instance(repositories.UsuariosRepository)
    usuario = repo.get_user_password(rut = data['rut'], password = hashlib.md5(data['password']))
    code = 0
    status = 400
    message = 'Error'
    data = None
    if usuario is not None:
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
    if usuario is not None:
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
    input_dto = dacite.from_dict(create_new_user.MenuInputDto, {
        'rut': data['rut'],
        'nombre': data['nombre'],
        'email': data['email'],
        'perfil_id': data['perfil_id'],
        'password': hashlib.md5(data['password']),
    })
    uc = create_new_user.MakeNewUserUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = UsuarioSerializer.serialize(output_dto.data)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')


@api_view(['POST'])
def create_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(create_new_menu.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menus': data['menus']
    })
    uc = create_new_menu.MakeNewMenuUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = UsuarioMenuSerializer.serialize(output_dto.data)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['POST'])
@serialize_exceptions
def select_menu_usuario(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(make_an_order.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menu_id': data['menu_id'],
        'descripcion': data['descripcion']
    })

    uc = make_an_order.MakeAnOrderUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = MultipleMenuSerializer.serialize(output_dto.data)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

@api_view(['POST'])
@serialize_exceptions
def confirmation_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(make_confirmation_menu.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menus_id': data['menus_id'],
        'status_id': os.environ['ESTATUS_CONFIRMATION']
    })

    uc = make_confirmation_menu.ConfirmationUseCase()
    output_dto = uc.execute(input_dto)
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = None).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

