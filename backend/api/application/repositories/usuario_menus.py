from abc import (
    ABCMeta,
    abstractmethod
)

from api.domain.entities import Menu, UsuarioMenu
from datetime import datetime
import typing
from datetime import datetime

class UsuarioMenusRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_menu_by_usuario_id(self, usuario_id: int, date: datetime) -> typing.List[Menu]:
        pass

    @abstractmethod
    def get_menu_usuario_by_fecha(self, date: datetime) -> typing.List[UsuarioMenu]:
        pass

    @abstractmethod
    def save(self, usuario_menu: UsuarioMenu) -> UsuarioMenu: 
        pass
