from typing import Optional

from datetime import datetime

class Menu:
    def __init__(self, id: Optional[int], descripcion: str, entrada: str, ensalada: str, plato_fondo: str, postre: str, fecha_registro: datetime, usuario_creacion_id: int, fecha_menu: datetime, status_id: int, orden: int ) -> None:
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
    def orden(self):
        return self._orden
        
    def setStatus(self, status_id):
        self._status_id = status_id
