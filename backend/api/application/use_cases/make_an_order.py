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
    menu_id: int
    descripcion: str

@dataclass
class MenuMakeOutputDto:
    code: int
    status: int
    message: str
    data: UsuarioMenu


class MakeAnOrderUseCase:
    menu_repo: MenusRepository = inject.attr(MenusRepository)
    usuario_menu_repo: UsuarioMenusRepository = inject.attr(UsuarioMenusRepository)
    usuario_repo: UsuariosRepository = inject.attr(UsuariosRepository)

    def execute(self, input_dto: MenuInputDto) -> MenuMakeOutputDto:
        code = 0
        data = None
        status = 400
        message = ""
        menu = self.menu_repo.get_by_id(input_dto.menu_id)
        usuario = self.usuario_repo.get_by_id(input_dto.usuario_id)
        usuario_menu = None
        if menu is not None:
            if usuario is not None:
                usuario_menu = self.usuario_menu_repo.save(UsuarioMenu(None, usuario.id, menu.id, input_dto.descripcion, date.today()))
                if usuario_menu is not None:
                    code = 1
                    status = 200
                    message = "Menu tomado correctamente"
                else:
                    code = 0
                    status = 500
                    message = "Error al crear menu"
            else:
                code = 0
                status = 500
                message = "Usuario no encontrado"
        else:
            code = 0
            status = 500
            message = "Menu no encontrado"
        
        return MenuMakeOutputDto(
            code,
            status,
            message,
            usuario_menu
        )
        #self.presenter.present(output_dto)
