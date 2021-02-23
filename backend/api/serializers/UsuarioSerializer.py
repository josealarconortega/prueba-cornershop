class MultipleUsuarioSerializer:

    @staticmethod
    def serialize(usuarios):
        return [UsuarioSerializer.serialize(usuario) for usuario in usuarios]

class UsuarioSerializer:
    @staticmethod
    def serialize(usuario):
        return {
            'id': usuario.id,
            'rut': usuario.rut,
            'nombre': usuario.nombre,
            'usuario_slack': usuario.usuario_slack,
            'fecha_registro': usuario.fecha_registro,
            'uid': usuario.uid,
            'perfil_id': usuario.perfil_id,
            'password': usuario.password
        }

