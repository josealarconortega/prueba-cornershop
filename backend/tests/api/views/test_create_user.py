import pytest
from django.test import Client
from django.urls import reverse

from api.models import Usuario as UsuarioModel
import json

@pytest.mark.usefixtures('transactional_db')
def test_create_user_success(
        usuario_with: UsuarioModel, password: str
) -> None:
    url = reverse('create_user')
    data = json.dumps({
        'rut': '11.111.111-1',
        'nombre': 'test',
        'email': 'test@test.cl',
        'perfil_id': usuario_with.perfil.id,
        'password': 'qwerty'
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

@pytest.mark.usefixtures('transactional_db')
def test_create_user_not_perfil(
        usuario_with: UsuarioModel, password: str
) -> None:
    url = reverse('create_user')
    data = json.dumps({
        'rut': '11.111.111-1',
        'nombre': 'test',
        'email': 'test@test.cl',
        'perfil_id': 0,
        'password': 'qwerty'
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 0
    assert output_dto['status'] == 500
