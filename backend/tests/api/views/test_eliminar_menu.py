import pytest
from django.test import Client, override_settings, TestCase
from django.urls import reverse

from api.models import Menu as MenuModel
import json
from unittest.mock import Mock, PropertyMock
from django.test import TestCase, RequestFactory
from django.conf import settings


@pytest.mark.usefixtures('transactional_db')
def test_eliminar_menu_passed(
        menu_with: MenuModel,
        menu_repo_mock: Mock
) -> None:
    url = reverse('eliminar_menu', args=[menu_with.id])
    response = Client().delete(url, None, content_type='application/json').content.decode()
    output_dto = json.loads(response)
    assert output_dto['code'] == 1
    assert output_dto['status'] == 200

@pytest.mark.usefixtures('transactional_db')
def test_eliminar_menu_failed(
        menu_confirmation_with: MenuModel,
        menu_repo_mock: Mock
) -> None:
        settings.STATUS_CONFIRMATION = menu_confirmation_with.status_id
        url = reverse('eliminar_menu', args=[menu_confirmation_with.id])
        response = Client().delete(url, None, content_type='application/json').content.decode()
        output_dto = json.loads(response)
        assert output_dto['code'] == 0
        assert output_dto['status'] == 400

#@pytest.mark.usefixtures('transactional_db')
#def test_login_required_credential_incorrect(
#        usuario_with: UsuarioModel, perfil_mantencion_with: PerfilModel
#) -> None:
#    url = reverse('login_required')
#    data = json.dumps({
#        'rut': str(usuario_with.rut),
#        'password': 'asd',
#        'perfil_id': perfil_mantencion_with.id
#    })
#    response = Client().post(url, data, content_type='application/json').content.decode()
#    output_dto = json.loads(response)
#    assert output_dto['code'] == 0
#    assert output_dto['status'] == 500

