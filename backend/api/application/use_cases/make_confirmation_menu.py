import abc
from dataclasses import dataclass

import inject

from api.application.repositories import MenusRepository, UsuarioMenusRepository, UsuariosRepository
from api.application.ports import SlackGateway
from api.domain.entities import Menu, UsuarioMenu
from datetime import date
import typing
from django.conf import settings
import os

@dataclass
class MenuInputDto:
    perfil_id: int
    menu_ids: typing.List[int]
    status_id: int

@dataclass
class MenuMakeOutputDto:
    code: int
    status: int
    message: str
    data: any


class ConfirmationUseCase:
    menu_repo: MenusRepository = inject.attr(MenusRepository)
    usuario_menu_repo: UsuarioMenusRepository = inject.attr(UsuarioMenusRepository)
    usuario_repo: UsuariosRepository = inject.attr(UsuariosRepository)

    slack_gateway: SlackGateway = inject.attr(SlackGateway)

    #@inject.params(presenter=PlacingBidOutputBoundary)
    #def __init__(self, presenter: PlacingBidOutputBoundary) -> None:
    #    self.presenter = presenter
    #@serialize_exceptions
    def execute(self, input_dto: MenuInputDto) -> MenuMakeOutputDto:
        code = 0
        data = None
        status = 400
        message = "" 
        usuarios = self.usuario_repo.get_all_by_perfil(input_dto.perfil_id)
        menus = self.menu_repo.get_by_id_list(input_dto.menu_ids)
        menuSTR = ""
        i = 1
        if menus is not None and usuarios is not None :
            for menu in menus:
                menu.setStatus(input_dto.status_id)
                menu = self.menu_repo.update(menu)
                menuSTR += "Opcion " + str(i) \
                + (",entrada " + str(menu.entrada) if menu.entrada is not None else '') \
                + (", plato fondo " + str(menu.plato_fondo) if menu.plato_fondo is not None else '') \
                + (", ensalada "+ str(menu.ensalada) if menu.ensalada is not None else '') \
                + (", postre " + str(menu.postre) if menu.postre is not None else '' ) \
                + ". \n" 
                i += 1
            i = 0
            for usuario in usuarios:
                msg = "Hola! Comparto con ustedes el menú de hoy \n " + menuSTR + " Para seleccionar el menu, debes ingresar al siguiente link " + settings.URL_SELECCION_MENU + usuario.uid
                if self.slack_gateway.notify_user(usuario.email, msg) == False:
                    i += 1
            if i == 0 :
                code = 0
                status = 500
                message = "Ocurrio un error al enviar mensaje a SLACK"
            else:
                code = 1
                status = 200
                message = "Mensajes enviados correctamente"
        else:
            code = 0
            status = 500
            message = "Ocurrio un error al obtener la informacion"
        
        return MenuMakeOutputDto(
            code,
            status,
            message,
            None
        )