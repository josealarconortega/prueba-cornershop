from django.apps import AppConfig

import inject

from api.application.ports import SlackGateway
from api.application.repositories import UsuariosRepository, MenusRepository, UsuarioMenusRepository, PerfilRepository
from api.infrastructure.adapters import SlackGatewayAdapter
from api.infrastructure.repositories import  DjangoORMUsuariosRepository, DjangoORMUsuarioMenusRepository, DjangoORMMenusRepository, DjangoORMPerfilRepository
def inject_config(binder: inject.Binder) -> None:
    binder.bind(SlackGateway, SlackGatewayAdapter())
    binder.bind(UsuariosRepository, DjangoORMUsuariosRepository())
    binder.bind(MenusRepository, DjangoORMMenusRepository())
    binder.bind(UsuarioMenusRepository, DjangoORMUsuarioMenusRepository())
    binder.bind(PerfilRepository, DjangoORMPerfilRepository())

class ApiConfig(AppConfig):
    name = 'api'
    