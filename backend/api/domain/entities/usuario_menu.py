from typing import Optional

from api.domain.entities.usuario import Usuario
from api.domain.entities.menu import Menu

class UsuarioMenu:
    def __init__(self, id: Optional[int], usuario_id: int, menu_id: int, observacion: str, fecha_registro) -> None:
        self._id = id
        self._usuario_id = usuario_id
        self._menu_id = menu_id
        self._observacion = observacion
        self._fecha_registro = fecha_registro
    @property
    def id(self):
        return self._id

    @property
    def usuario_id(self):
        return self._usuario

    @property
    def menu_id(self):
        return self._menu_id

    @property
    def observacion(self):
        return self._observacion

    @property
    def fecha_registro(self):
        return self._fecha_registro

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other