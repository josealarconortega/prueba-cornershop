import pytest
from django.test import Client
from django.urls import reverse

from api.models import UsuarioMenu as UsuarioMenuModel
import json
from unittest.mock import Mock, PropertyMock
from django.test import TestCase, RequestFactory

@pytest.mark.usefixtures('transactional_db')
def test_menu_usuario_id_fecha_passed(
        usuario_menu_with: UsuarioMenuModel
) -> None:
    url = reverse('obtener_menus_usuario_fecha')
    data = json.dumps({
        'fecha_menu': usuario_menu_with.menu.fecha_menu.strftime("%Y-%m-%d %H:%M:%S")
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200
