import pytest
from django.test import Client
from django.urls import reverse

from api.models import (Menu as MenuModel,
                        Usuario as UsuarioModel)
import json
import datetime

@pytest.mark.usefixtures('transactional_db')
def test_select_menu_usuario_success(
        usuario_empleado_with: UsuarioModel, menu_with: MenuModel
) -> None:
    url = reverse('select_menu_usuario')
    data = json.dumps({
        'user_id': usuario_empleado_with.id,
        'menu_id':  menu_with.id,
        'descripcion': 'TEST'
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200
