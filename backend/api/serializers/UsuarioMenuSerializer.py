class MultipleUsuarioMenuSerializer:

    @staticmethod
    def serialize(usuario_menus):
        return [UsuarioMenuSerializer.serialize(usuario_menu) for usuario_menu in usuario_menus]

class UsuarioMenuSerializer:

    @staticmethod
    def serialize(usuario_menu):
        return {
                'id': usuario_menu.id,
                'observacion': usuario_menu.observacion,
                'usuario_id': usuario_menu.usuario_id,
                'menu_id': usuario_menu.menu_id,
                'fecha_registro': usuario_menu.fecha_registro.strftime("%Y%M%D %H:%M:%S"),
            }

