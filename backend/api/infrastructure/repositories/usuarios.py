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
                fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, perfil_descripcion = usuario_model.perfil.descripcion, password = usuario_model.password
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
                perfil_id = usuario_model.perfil.id, perfil_descripcion = usuario_model.perfil.descripcion, password = usuario_model.password)
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
                perfil_id = usuario_model.perfil.id, perfil_descripcion = usuario_model.perfil.descripcion, password = usuario_model.password)
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
                fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, perfil_descripcion = usuario_model.perfil.descripcion, password = usuario_model.password
            )
        except Exception as e:
            return None

    def get_user_password(self, rut: str, password: str, perfil_id: int) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuario_model = UsuarioModel.objects.filter(rut = rut, password = password, perfil_id = perfil_id).first()
            if usuario_model is not None:
                return Usuario(
                    id = usuario_model.id, rut = usuario_model.rut, nombre = usuario_model.nombre, email = usuario_model.email, 
                    fecha_registro = usuario_model.fecha_registro, uid = usuario_model.uid, perfil_id = usuario_model.perfil.id, 
                    perfil_descripcion = usuario_model.perfil.descripcion, password = usuario_model.password
                )
            else:
                return None
        except Exception as e:
            return None

    def update(self, usuario: Usuario) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            usuario_model = UsuarioModel.objects.get(id=usuario.id)
            perfil_instance = PerfilModel.objects.get(id=usuario.perfil_id)

            usuario_model.rut = usuario.rut
            usuario_model.nombre = usuario.nombre
            usuario_model.email = usuario.email
            usuario_model.perfil = perfil_instance
            usuario_model.password = usuario.password
            usuario_model.save()
            return usuario

        except Exception as e:
            return None

    def save(self, usuario: Usuario) -> Usuario:
        from api.models import Usuario as UsuarioModel
        from api.models import Perfil  as PerfilModel
        try:
            perfil_instance = PerfilModel.objects.get(id=usuario.perfil_id)
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

    def delete(self, usuario_id: int) -> bool: 
        from api.models import (
            Usuario as UsuarioModel
        )
        try:
            usuario_model = UsuarioModel.objects.get(id=usuario_id)
            usuario_model.delete()
            return True
        except Exception as e:
            return False
