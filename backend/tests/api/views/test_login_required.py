import pytest
from django.test import Client
from django.urls import reverse

from api.models import Usuario as UsuarioModel
import json

@pytest.mark.usefixtures('transactional_db')
def test_login_required_passed(
        usuario_with: UsuarioModel, password: str
) -> None:
    url = reverse('login_required')
    data = json.dumps({
        'rut': str(usuario_with.rut),
        'password': str(password)
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

@pytest.mark.usefixtures('transactional_db')
def test_login_required_credential_incorrect(
        usuario_with: UsuarioModel
) -> None:
    url = reverse('login_required')
    data = json.dumps({
        'rut': str(usuario_with.rut),
        'password': 'asd'
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 0
    assert output_dto['status'] == 500

