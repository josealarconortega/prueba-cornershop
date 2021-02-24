from typing import Optional

from api.domain.entities.perfil import Perfil
from api.domain.entities.menu import Menu

class Usuario:
    def __init__(self, id: Optional[int], nombre: str, rut: str, email: str, fecha_registro: str, uid: str, perfil_id: int, password: str) -> None:
        self._id = id
        self._rut = rut
        self._nombre = nombre
        self._email = email
        self._fecha_registro = fecha_registro
        self._uid = uid
        self._perfil_id = perfil_id
        self._password = password
    @property
    def id(self):
        return self._id

    @property
    def rut(self):
        return self._rut

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @property
    def uid(self):
        return self._uid

    @property
    def perfil_id(self):
        return self._perfil_id

    @property
    def password(self):
        return self._password

    def __str__(self):
        return f'<Usuario #{self._id}>'
