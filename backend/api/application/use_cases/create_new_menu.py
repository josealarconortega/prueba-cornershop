import abc
from dataclasses import dataclass

import inject

from api.application.repositories import MenusRepository, UsuarioMenusRepository, UsuariosRepository
from api.application.ports import SlackGateway
from api.domain.entities import Menu, UsuarioMenu
from datetime import date

@dataclass
class MenuInputDto:
    usuario_id: int
    descripcion: str
    entrada: str
    ensalada: str
    plato_fondo: str
    postre: str

@dataclass
class MenuMakeOutputDto:
    code: int
    status: int
    message: str
    data: Menu

class MakeNewMenuUseCase:
    menu_repo: MenusRepository = inject.attr(MenusRepository)
    #usuario_menu_repo: UsuarioMenusRepository = inject.attr(UsuarioMenusRepository)
    usuario_repo: UsuariosRepository = inject.attr(UsuariosRepository)

    slack_gateway: SlackGateway = inject.attr(SlackGateway)

    def execute(self, input_dto: MenuInputDto) -> MenuMakeOutputDto:

        code = 0
        data = None
        status = 400
        message = ""
        menu = self.menu_repo.save()
        usuario = self.usuario_repo.get_by_id(input_dto.usuario_id)

