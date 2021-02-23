from api.application.repositories import UsuariosRepository
from api.domain.entities import (
    Usuario,
    Perfil
)
import typing

class DjangoORMUsuariosRepository(UsuariosRepository):

    def get_by_id(self, usuario_id: int) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuario_model = UsuarioModel.objects.get(id=usuario_id)
            return Usuario(
                id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, email = usuario_model.email, 
                fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, password = usuario_model.password
            )
        except Exception as e:
            return None
    
    def get_all(self) -> typing.List[Usuario]:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuarios_model = UsuarioModel.objects.all()
            return [
                Usuario(id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, 
                email = usuario_model.email, fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, 
                perfil_id = usuario_model.perfil.id, password = usuario_model.password)
                for usuario_model in usuarios_model
            ]
        except Exception as e:
            return None
    def get_all_by_perfil(self, perfil_id: int) -> typing.List[Usuario]:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuarios_model = UsuarioModel.objects.filter(perfil_id = perfil_id).all()
            return [
                Usuario(id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, 
                email = usuario_model.email, fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, 
                perfil_id = usuario_model.perfil.id, password = usuario_model.password)
                for usuario_model in usuarios_model
            ]
        except Exception as e:
            return None

    def get_by_uid(self, uid: str) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuario_model = UsuarioModel.objects.get(uid=uid)
            return Usuario(
                id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, email = usuario_model.email, 
                fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, password = usuario_model.password
            )
        except Exception as e:
            return None

    def get_user_password(self, rut: str, password: str) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuario_model = UsuarioModel.objects.get(rut = rut, password = password)
            if len(usuario_model) > 0 :
                return Usuario(
                    id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, email = usuario_model.email, 
                    fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, password = usuario_model.password
                )
            else:
                return None
        except Exception as e:
            return None
    def save(self, usuario: Usuario) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            perfil_instance = PerfilModel.objects.get(id=Usuario.perfil_id)
            model = UsuarioModel(id = usuario.id,
                    rut = usuario.rut,
                    nombre = usuario.nombre,
                    email = usuario.email,
                    fecha_registro = usuario.fecha_registro,
                    uid = usuario.uid,
                    perfil = perfil_instance,
                    password = usuario.password)
            model.save()
            return usuario
        except Exception as e:
            return None