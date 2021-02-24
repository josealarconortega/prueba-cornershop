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
            'email': usuario.email,
            'fecha_registro': usuario.fecha_registro.strftime("%Y%M%D %H:%M:%S"),
            'uid': str(usuario.uid),
            'perfil_id': usuario.perfil_id,
            'password': usuario.password
        }

