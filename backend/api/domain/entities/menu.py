from typing import Optional

from datetime import datetime

class Menu:
    def __init__(self, id: Optional[int], descripcion: str, entrada: str, ensalada: str, plato_fondo: str, postre: str, fecha_registro: datetime, usuario_creacion_id: int, fecha_menu: datetime, status_id: int, status_descripcion: str, orden: int ) -> None:
        self._id = id
        self._descripcion = descripcion
        self._entrada = entrada
        self._ensalada = ensalada
        self._plato_fondo = plato_fondo
        self._postre = postre
        self._fecha_registro = fecha_registro
        self._usuario_creacion_id = usuario_creacion_id
        self._fecha_menu = fecha_menu
        self._status_id = status_id
        self._status_descripcion = status_descripcion
        self._orden = orden
    @property
    def id(self):
        return self._id

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def entrada(self):
        return self._entrada

    @property
    def ensalada(self):
        return self._ensalada

    @property
    def plato_fondo(self):
        return self._plato_fondo

    @property
    def postre(self):
        return self._postre


    @property
    def fecha_registro(self):
        return self._fecha_registro

    @property
    def usuario_creacion_id(self):
        return self._usuario_creacion_id
    
    @property
    def fecha_menu(self):
        return self._fecha_menu

    @property
    def status_id(self):
        return self._status_id

    @property
    def status_descripcion(self):
        return self._status_descripcion

    @property
    def orden(self):
        return self._orden

    def setId(self, menu_id: int):
        self._id = menu_id

    def setDescripcion(self, descripcion: str):
        self._descripcion = descripcion

    def setEntrada(self, entrada: str):
        self._entrada = entrada

    def setEnsalada(self, ensalada: str):
        self._ensalada = ensalada

    def setPlatoFondo(self, plato_fondo: str):
        self._plato_fondo = plato_fondo

    def setPostre(self, postre: str):
        self._postre = postre

    def setStatus(self, status_id):
        self._status_id = status_id
