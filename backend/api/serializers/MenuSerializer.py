class MultipleMenuSerializer:

    @staticmethod
    def serialize(menus):
        return [MenuSerializer.serialize(menu) for menu in menus]

class MenuSerializer:

    @staticmethod
    def serialize(menu):
        return {
                'id': menu.id,
                'descripcion': menu.descripcion,
                'entrada': menu.entrada,
                'ensalada': menu.ensalada,
                'plato_fondo': menu.plato_fondo,
                'postre': menu.postre,
                'fecha_registro': menu.fecha_registro.strftime("%Y%M%D %H:%M:%S"),
                'usuario_creacion_id':menu.usuario_creacion_id,
                'fecha_menu': menu.fecha_menu.strftime("%Y%M%D %H:%M:%S")
            }

