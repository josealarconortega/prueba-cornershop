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
from api.application.use_cases import make_an_order
from rest_framework.decorators import api_view,permission_classes
from config.decorators import serialize_exceptions
from api.serializers import UsuarioMenuSerializer, UsuarioSerializer
from api.domain.value_objects import Response
import hashlib 

@api_view(['POST'])
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
@api_view(['POST'])
def save_menu(request: HttpRequest) -> HttpResponse:
    data = json.loads(request.body)
    input_dto = dacite.from_dict(make_an_order.MenuInputDto, {
        'usuario_id': data['user_id'],
        'menu_id': data['menu_id'],
        'descripcion': data['descripcion']
    })
    pass
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
    response = Response(code=output_dto.code, status= output_dto.status, message = output_dto.message, data = UsuarioMenuSerializer.serialize(output_dto)).toResponse()
    return HttpResponse(response, status=output_dto.status, content_type='application/json')

