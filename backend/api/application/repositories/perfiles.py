from abc import (
    ABCMeta,
    abstractmethod
)

from api.domain.entities import Perfil
from datetime import datetime
import typing

class PerfilRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_by_id(self, id_perfil: int) -> typing.List[Perfil]:
        pass