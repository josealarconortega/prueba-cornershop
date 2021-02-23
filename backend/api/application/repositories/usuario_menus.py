from abc import (
    ABCMeta,
    abstractmethod
)

from api.domain.entities import Menu, UsuarioMenu
from datetime import datetime
import typing

class UsuarioMenusRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_menu_by_usuario_id(self, usuario_id: int) -> typing.List[Menu]:
        pass

    @abstractmethod
    def save(self, usuario_menu: UsuarioMenu) -> UsuarioMenu: 
        pass
