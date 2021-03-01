from typing import Optional

from api.domain.entities.perfil import Perfil
from api.domain.entities.menu import Menu

class Usuario:
    def __init__(self, id: Optional[int], rut: str, nombre: str, email: str, fecha_registro: str, uid: str, perfil_id: int, perfil_descripcion: str, password: str) -> None:
        self._id = id
        self._rut = rut
        self._nombre = nombre
        self._email = email
        self._fecha_registro = fecha_registro
        self._uid = uid
        self._perfil_id = perfil_id
        self._perfil_descripcion = perfil_descripcion
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
    def perfil_descripcion(self):
        return self._perfil_descripcion

    @property
    def password(self):
        return self._password

    def setId(self, menu_id: int):
        self._id = menu_id

    def setRut(self, rut: str):
        self._rut = rut

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def setEmail(self, email: str):
        self._email = email

    def setPerfilId(self, perfil_id: int):
        self._perfil_id = perfil_id

    def setPerfilDescripcion(self, perfil_descripcion: str):
        self._perfil_descripcion = perfil_descripcion

    def setPassword(self, password: str):
        self._password = password

    def __str__(self):
        return f'<Usuario #{self._id}>'
