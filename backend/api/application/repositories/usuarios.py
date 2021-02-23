from abc import (
    ABCMeta,
    abstractmethod
)

from api.domain.entities import Menu, Usuario
from datetime import datetime
import typing

class UsuariosRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, usuario_id: int) -> Usuario:
        pass

    @abstractmethod
    def get_all(self) -> typing.List[Usuario]:
        pass

    @abstractmethod
    def get_user_password(self, rut: str, password: str) -> Usuario:
        pass

    @abstractmethod
    def save(self, usuario: Usuario) -> Usuario:
        pass

