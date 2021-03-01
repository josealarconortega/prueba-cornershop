import pytest
from django.test import Client
from django.urls import reverse

from api.models import (Menu as MenuModel,
                        Status as StatusModel)
import json
import datetime

@pytest.mark.usefixtures('transactional_db')
def test_editar_menu_success(
        menu_with: MenuModel, status_registrado_with: StatusModel
) -> None:
    url = reverse('editar_menu')
    data = json.dumps({
        'user_id': menu_with.usuario_creacion.id,
        'menus': [
            {
                'menu_id': menu_with.id,
                'descripcion': 'descripcion',
                'entrada': 'entrada',
                'ensalada': 'ensalada',
                'plato_fondo': 'plato_fondo',
                'postre': 'postre',
                'status_id': status_registrado_with.id,
                'fecha_menu': '2021-01-01 00:00:00',
                'orden': 1,
            }
        ]
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

