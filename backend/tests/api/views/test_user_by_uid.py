import pytest
from django.test import Client
from django.urls import reverse

from api.models import Usuario as UsuarioModel
import json

@pytest.mark.usefixtures('transactional_db')
def test_user_by_uid_passed(
        usuario_with: UsuarioModel, uid: str
) -> None:
    url = reverse('user_by_uid', args=[uid]) 
    response = Client().get(url, None, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

@pytest.mark.usefixtures('transactional_db')
def test_user_by_uid_not_fount(
        usuario_with: UsuarioModel
) -> None:
    url = reverse('user_by_uid', args=['a']) 
    response = Client().get(url, None, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 0
    assert output_dto['status'] == 500

