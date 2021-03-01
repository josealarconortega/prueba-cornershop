from typing import Optional

from api.domain.entities.usuario import Usuario
from api.domain.entities.menu import Menu

class UsuarioMenu:
    def __init__(self, id: Optional[int] = None, usuario_id: int  = None , menu_id: int  = None , observacion: str  = None , fecha_registro  = None , usuario: Usuario  = None , menu: Menu = None) -> None:
        self._id = id
        self._usuario_id = usuario_id
        self._menu_id = menu_id
        self._observacion = observacion
        self._fecha_registro = fecha_registro
        self._usuario = usuario
        self._menu = menu
    @property
    def id(self):
        return self._id

    @property
    def usuario_id(self):
        return self._usuario_id

    @property
    def menu_id(self):
        return self._menu_id

    @property
    def observacion(self):
        return self._observacion

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @property
    def usuario(self):
        return self._usuario

    @property
    def menu(self):
        return self._menu

    def setgetByUsuarioMenuModel(self, usuarioMenuModel):
        from api.models import UsuarioMenu as UsuarioMenuModel
        menu = Menu(id = usuarioMenuModel.menu.id, descripcion = usuarioMenuModel.menu.descripcion, entrada = usuarioMenuModel.menu.entrada,  
        ensalada = usuarioMenuModel.menu.ensalada, plato_fondo = usuarioMenuModel.menu.plato_fondo, postre = usuarioMenuModel.menu.postre,
        fecha_registro = usuarioMenuModel.menu.fecha_registro, usuario_creacion_id = usuarioMenuModel.menu.usuario_creacion.id , 
        fecha_menu = usuarioMenuModel.menu.fecha_menu, status_id = usuarioMenuModel.menu.status.id, status_descripcion = usuarioMenuModel.menu.status.descripcion, orden = usuarioMenuModel.menu.orden )
        usuario = Usuario(id = usuarioMenuModel.usuario.id, rut = usuarioMenuModel.usuario.rut, nombre = usuarioMenuModel.usuario.nombre,  
        email = usuarioMenuModel.usuario.email, fecha_registro = usuarioMenuModel.usuario.fecha_registro, uid = usuarioMenuModel.usuario.uid,
        perfil_id = usuarioMenuModel.usuario.perfil.id, perfil_descripcion = usuarioMenuModel.usuario.perfil.descripcion , 
        password = usuarioMenuModel.usuario.password)
        self._id = usuarioMenuModel.id
        self._usuario_id = usuarioMenuModel.usuario.id
        self._menu_id = usuarioMenuModel.menu.id
        self._observacion = usuarioMenuModel.observacion
        self._fecha_registro = usuarioMenuModel.fecha_registro
        self._usuario = usuario
        self._menu = menu
        return self