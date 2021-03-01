import pytest
from django.test import Client
from django.urls import reverse

from api.models import Usuario as UsuarioModel
import json
from unittest.mock import Mock, PropertyMock
from django.test import TestCase, RequestFactory

@pytest.mark.usefixtures('transactional_db')
def test_obtener_usuarios_passed(
        usuario_with: UsuarioModel
) -> None:
    url = reverse('obtener_usuarios')
    response = Client().get(url, None, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200