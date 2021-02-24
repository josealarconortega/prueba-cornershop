import pytest
from django.test import Client
from django.urls import reverse

from api.models import (Menu as MenuModel,
                        Usuario as UsuarioModel,
                        Status as StatusModel,
                        Perfil as PerfilModel)
import json
import datetime
from unittest.mock import (
    Mock,
    patch,
)
@pytest.mark.usefixtures('transactional_db')
def test_select_menu_usuario_success(
        perfil_empleado_with: PerfilModel, menu_with: MenuModel, status_confirmado_with: StatusModel
) -> None:
    url = reverse('confirmation_menu')
    data = json.dumps({
        'perfil_id': perfil_empleado_with.id,
        'menu_ids':  [menu_with.id],
        'status_id': status_confirmado_with.id
    })
    response = Client().post(url, data, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    
    assert output_dto['code'] == 0
    assert output_dto['status'] == 500
