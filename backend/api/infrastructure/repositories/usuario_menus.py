import typing
from api.application.repositories import UsuarioMenusRepository
from api.domain.entities import (
    Perfil,
    Usuario,
    Menu,
    UsuarioMenu
)


from datetime import datetime

class DjangoORMUsuarioMenusRepository(UsuarioMenusRepository):

    def get_menu_by_usuario_id(self, usuario_id: int, date: datetime) -> typing.List[Menu]:
        from api.models import UsuarioMenu as UsuarioMenuModel
        from api.models import Usuario as UsuarioModel
        from api.models import Menu as MenuModel
        try:
            usuario_menu_models = UsuarioMenuModel.objects.select_related('usuario').filter(usuario__id = usuario_id, menu__fecha_menu__year=date.year,
            menu__fecha_menu__month=date.month,
            menu__fecha_menu__day=date.day)
            return [
                UsuarioMenu().setgetByUsuarioMenuModel(usuario_menu_model_data).menu
                for usuario_menu_model_data in usuario_menu_models
                #Menu(id = menu_model_data.menu.id, descripcion = menu_model_data.menu.descripcion, entrada = menu_model_data.menu.entrada,  
                #ensalada = menu_model_data.menu.ensalada, plato_fondo = menu_model_data.menu.plato_fondo, postre = menu_model_data.menu.postre,
                #fecha_registro = menu_model_data.menu.fecha_registro, usuario_creacion_id = menu_model_data.menu.usuario_creacion.id , 
                #fecha_menu = menu_model_data.menu.fecha_menu, status_id = menu_model_data.menu.status.id, status_descripcion = menu_model_data.menu.status.descripcion, orden = menu_model_data.menu.orden )
                #for menu_model_data in usuario_menu_models
            ]
        except Exception as e:
            return None

    def get_menu_usuario_by_fecha(self, date: datetime) -> typing.List[UsuarioMenu]:
        from api.models import UsuarioMenu as UsuarioMenuModel
        try:
            usuario_menu_models = UsuarioMenuModel.objects.filter(menu__fecha_menu__year=date.year,
            menu__fecha_menu__month=date.month,
            menu__fecha_menu__day=date.day)
            
            return [
                UsuarioMenu().setgetByUsuarioMenuModel(usuario_menu_model_data)
                for usuario_menu_model_data in usuario_menu_models
            ]
        except Exception as e:
            return None

    def save(self, usuario_menu: UsuarioMenu) -> UsuarioMenu: 
        from api.models import UsuarioMenu as UsuarioMenuModel
        from api.models import Usuario as UsuarioModel
        from api.models import Menu as MenuModel
        try:
            usuario_instance = UsuarioModel.objects.get(id=usuario_menu.usuario_id)
            menu_instance = MenuModel.objects.get(id=usuario_menu.menu_id)
            
            model = UsuarioMenuModel(usuario = usuario_instance, menu = menu_instance,  
                observacion = usuario_menu.observacion, fecha_registro = usuario_menu.fecha_registro)
            model.save()
            return usuario_menu
        except Exception as e:
            return None
            