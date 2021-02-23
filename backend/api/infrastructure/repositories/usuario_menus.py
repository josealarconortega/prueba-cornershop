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

    def get_menu_by_usuario_id(self, usuario_id: int) -> typing.List[Menu]:
        from api.models import UsuarioMenu as UsuarioMenuModel
        from api.models import Usuario as UsuarioModel
        from api.models import Menu as MenuModel
        try:
            usuario_menu_models = UsuarioMenuModel.objects.select_related('usuario').filter(usuario__id = usuario_id)
            return [
                Menu(id = usuario_menu_models.menu.id, descripcion = usuario_menu_models.menu.descripcion, entrada = usuario_menu_models.menu.entrada,  
                ensalada = usuario_menu_models.menu.ensalada, plato_fondo = usuario_menu_models.menu.plato_fondo, postre = usuario_menu_models.menu.postre,
                fecha_registro = usuario_menu_models.menu.fecha_registro, usuario_creacion = usuario_menu_models.menu.usuario_creacion.id , fecha_menu = usuario_menu_models.menu.fecha_menu)
                for menu_model_data in usuario_menu_models
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
            model = UsuarioMenuModel(id = usuario_menu.id,usuario = usuario_instance, menu = menu_instance,  
                observacion = UsuarioMenu.observacion, fecha_menu = usuario_menu.fecha_registro)
            model.save()
            return usuario_menu
        except Exception as e:
            return None
            