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
            menus_model = MenuModel.objects.all().order_by('orden')
            return [
                Menu(id = menu_model.id, descripcion = menu_model.descripcion, entrada = menu_model.entrada,  
                ensalada = menu_model.ensalada, plato_fondo = menu_model.plato_fondo, postre = menu_model.postre,
                fecha_registro = menu_model.fecha_registro, usuario_creacion_id = menu_model.usuario_creacion.id , fecha_menu = menu_model.fecha_menu, 
                status_id = menu_model.status.id, status_descripcion = menu_model.status.descripcion, orden = menu_model.orden )
                for menu_model in menus_model
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
            menu_model = MenuModel.objects.get(id = menu_id)
            return Menu(id = menu_model.id, descripcion = menu_model.descripcion, entrada = menu_model.entrada,  
                ensalada = menu_model.ensalada, plato_fondo = menu_model.plato_fondo, postre = menu_model.postre,
                fecha_registro = menu_model.fecha_registro, usuario_creacion_id = menu_model.usuario_creacion.id, 
                fecha_menu = menu_model.fecha_menu, status_id = menu_model.status.id, status_descripcion = menu_model.status.descripcion, orden = menu_model.orden)
        except Exception as e:
            return None
    
    def get_by_id_list(self, menu_id_list: typing.List[int]) -> typing.List[Menu]:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menus_model = MenuModel.objects.filter(id__in = menu_id_list).order_by('orden')
            return [
                Menu(id = menu_model.id, descripcion = menu_model.descripcion, entrada = menu_model.entrada,  
                ensalada = menu_model.ensalada, plato_fondo = menu_model.plato_fondo, postre = menu_model.postre,
                fecha_registro = menu_model.fecha_registro, usuario_creacion_id = menu_model.usuario_creacion.id , fecha_menu = menu_model.fecha_menu, 
                status_id = menu_model.status.id, status_descripcion = menu_model.status.descripcion, orden = menu_model.orden )
                for menu_model in menus_model
            ]
        except Exception as e:
            return None

    def get_by_date(self, date: datetime ) -> typing.List[Menu]:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menus_model = MenuModel.objects.filter(fecha_menu__year=date.year,
                                  fecha_menu__month=date.month,
                                  fecha_menu__day=date.day).order_by('orden')
            return [
                    Menu(id = menu_model.id, descripcion = menu_model.descripcion, entrada = menu_model.entrada,  
                    ensalada = menu_model.ensalada, plato_fondo = menu_model.plato_fondo, postre = menu_model.postre,
                    fecha_registro = menu_model.fecha_registro, usuario_creacion_id = menu_model.usuario_creacion.id , fecha_menu = menu_model.fecha_menu, 
                    status_id = menu_model.status.id, status_descripcion = menu_model.status.descripcion, orden = menu_model.orden )
                    for menu_model in menus_model
                ]
        except Exception as e:
            return None

    def get_by_date_status(self, date: datetime, status_id: int ) -> typing.List[Menu]:
        from api.models import (
            Menu as MenuModel,
            Usuario as UsuarioModel,
            Status as StatusModel
        )
        try:
            menus_model = MenuModel.objects.filter(fecha_menu__year=date.year,
                                  fecha_menu__month=date.month,
                                  fecha_menu__day=date.day, status_id = status_id).order_by('orden')
            return [
                    Menu(id = menu_model.id, descripcion = menu_model.descripcion, entrada = menu_model.entrada,  
                    ensalada = menu_model.ensalada, plato_fondo = menu_model.plato_fondo, postre = menu_model.postre,
                    fecha_registro = menu_model.fecha_registro, usuario_creacion_id = menu_model.usuario_creacion.id , fecha_menu = menu_model.fecha_menu, 
                    status_id = menu_model.status.id, status_descripcion = menu_model.status.descripcion, orden = menu_model.orden )
                    for menu_model in menus_model
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
            menu_model = MenuModel.objects.get(id=menu.id)
            usuario_instance = UsuarioModel.objects.get(id=menu.usuario_creacion_id)
            status_instance = StatusModel.objects.get(id=menu.status_id)
            menu_model.descripcion = menu.descripcion
            menu_model.entrada = menu.entrada
            menu_model.ensalada = menu.ensalada
            menu_model.plato_fondo = menu.plato_fondo
            menu_model.postre = menu.postre
            menu_model.fecha_registro = menu.fecha_registro
            menu_model.usuario_creacion = usuario_instance
            menu_model.fecha_menu = menu.fecha_menu
            menu_model.status = status_instance
            menu_model.orden = menu.orden
            menu_model.save()
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
            menu_model = MenuModel(descripcion = menu.descripcion, entrada = menu.entrada,  
                ensalada = menu.ensalada, plato_fondo = menu.plato_fondo, postre = menu.postre,
                fecha_registro = menu.fecha_registro, usuario_creacion = usuario_instance , fecha_menu = menu.fecha_menu, status = status_instance, orden = menu.orden)
            menu_model.save()
            menu.setId(menu_model.id)
            return menu
        except Exception as e:
            return None

    def delete(self, menu_id: int) -> bool: 
        from api.models import (
            Menu as MenuModel
        )
        try:
            menu_model = MenuModel.objects.get(id=menu_id)
            menu_model.delete()
            return True
        except Exception as e:
            return False
