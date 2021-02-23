import typing
from api.application.repositories import MenusRepository
from api.domain.entities import (
    Perfil,
    Usuario,
    Menu,
    UsuarioMenu
)

from datetime import datetime

class DjangoORMMenusRepository(MenusRepository):

    def get_all(self) -> typing.List[Menu]:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menus_model = MenuModel.objects.all()
            return [
                Menu(id = menu_model_data.id, descripcion = menu_model_data.descripcion, entrada = menu_model_data.entrada,  
                ensalada = menu_model_data.ensalada, plato_fondo = menu_model_data.plato_fondo, postre = menu_model_data.postre,
                fecha_registro = menu_model_data.fecha_registro, usuario_creacion_id = menu_model_data.usuario_creacion.id , fecha_menu = menu_model_data.fecha_menu, status_id = menu_model_data.status.id )
                for menu_model_data in menus_model
            ]
        except Exception as e:
            return None

    def get_by_id(self, menu_id: int) -> Menu:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menu = MenuModel.objects.get(id = menu_id)
            return Menu(id = menu.id, descripcion = menu.descripcion, entrada = menu.entrada,  
                ensalada = menu.ensalada, plato_fondo = menu.plato_fondo, postre = menu.postre,
                fecha_registro = menu.fecha_registro, usuario_creacion_id = menu.usuario_creacion.id , fecha_menu = menu.fecha_menu, status_id = menu.status.id)
        except Exception as e:
            return None
    def get_by_date(self, date: datetime ) -> typing.List[Menu]:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menus_model = MenuModel.objects.get(fecha_registro=date).all()
            return [
                    Menu(id = menu_model_data.id, descripcion = menu_model_data.descripcion, entrada = menu_model_data.entrada,  
                    ensalada = menu_model_data.ensalada, plato_fondo = menu_model_data.plato_fondo, postre = menu_model_data.postre,
                    fecha_registro = menu_model_data.fecha_registro, usuario_creacion_id = menu_model_data.usuario_creacion.id , fecha_menu = menu_model_data.fecha_menu, status_id = menu_model_data.status.id)
                    for menu_model_data in menus_model
                ]
        except Exception as e:
            return None

    def update(self, menu: Menu) -> Menu:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menu_instance = MenuModel.objects.get(id=menu.id)
            usuario_instance = UsuarioModel.objects.get(id=menu.usuario_creacion_id)
            status_instance = StatusModel.objects.get(id=menu.status_id)
            menu_instance.descripcion = menu.descripcion
            menu_instance.entrada = menu.entrada
            menu_instance.ensalada = menu.ensalada
            menu_instance.plato_fondo = menu.plato_fondo
            menu_instance.postre = menu.postre
            menu_instance.fecha_registro = menu.fecha_registro
            menu_instance.usuario_creacion = usuario_instance
            menu_instance.fecha_menu = menu.fecha_menu
            menu_instance.status = status_instance
            menu_instance.save()
            return menu
        except Exception as e:
            return None
    
    def save(self, menu: Menu) -> Menu: 
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            usuario_instance = UsuarioModel.objects.get(id=menu.usuario_creacion_id)
            status_instance = StatusModel.objects.get(id=menu.status_id)
            model = MenuModel(id = menu.id, descripcion = menu.descripcion, entrada = menu.entrada,  
                ensalada = menu.ensalada, plato_fondo = menu.plato_fondo, postre = menu.postre,
                fecha_registro = menu.fecha_registro, usuario_creacion = usuario_instance , fecha_menu = menu.fecha_menu, status = status_instance)
            model.save()
            return menu
        except Exception as e:
            return None

