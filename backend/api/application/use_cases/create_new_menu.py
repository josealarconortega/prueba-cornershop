import abc
from dataclasses import dataclass

import inject

from api.application.repositories import MenusRepository, UsuarioMenusRepository, UsuariosRepository
from api.application.ports import SlackGateway
from api.domain.entities import Menu, UsuarioMenu
from datetime import date
import typing
@dataclass
class MenuDescripcionDTO:
    descripcion: str
    entrada: str
    ensalada: str
    plato_fondo: str
    postre: str
    status_id: str
@dataclass
class MenuInputDto:
    usuario_id: int
    menus: typing.List[MenuDescripcionDTO]

@dataclass
class MenuMakeOutputDto:
    code: int
    status: int
    message: str
    data: typing.List[Menu]

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
        usuario = self.usuario_repo.get_by_id(input_dto.usuario_id)
        menu = None
        if usuario is not None:
            i = 0
            menus = []
            for menu in input_dto.menus:
                menu = self.menu_repo.save(Menu(None, menu.descripcion, menu.entrada, menu.ensalada, menu.plato_fondo, menu.postre, date.today(), input_dto.usuario_id, menu.fecha_menu, menu.status_id, menu.orden))
                if menu is not None:
                    menus.append(menu)
                    i += 1 
            if i == len(input_dto.menus) and i > 0:
                code = 1
                status = 200
                message = "Menu registrado correctamente"
            else:
                code = 0
                status = 500
                message = "Error al registrar menu"
        else:
            code = 0
            status = 500
            message = "Error al registrar menu"

        return MenuMakeOutputDto(
            code,
            status,
            message,
            menus
        )