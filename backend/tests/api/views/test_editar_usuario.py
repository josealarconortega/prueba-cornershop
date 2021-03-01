import pytest
from django.test import Client
from django.urls import reverse

from api.models import Usuario as UsuarioModel
import json
import datetime

@pytest.mark.usefixtures('transactional_db')
def test_editar_usuario_success(
        usuario_with: UsuarioModel
) -> None:
    url = reverse('editar_usuario')
    data = json.dumps({
        'usuario_id': usuario_with.id,
        'rut': '11.111.111-1',
        'nombre': 'nombre',
        'email': 'email@email.cl',
        'perfil_id': usuario_with.perfil_id,
        'password': 'qwerty123' 
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

