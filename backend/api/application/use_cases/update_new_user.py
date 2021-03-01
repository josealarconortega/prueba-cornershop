import abc
from dataclasses import dataclass

import inject

from api.application.repositories import MenusRepository, UsuarioMenusRepository, UsuariosRepository, PerfilRepository
from api.application.ports import SlackGateway
from api.domain.entities import Usuario
from datetime import date
import typing
import uuid
@dataclass
class MenuInputDto:
    usuario_id: int
    rut: str
    nombre: str
    email: str
    perfil_id: int
    password: str


@dataclass
class UserMakeOutputDto:
    code: int
    status: int
    message: str
    data: Usuario

class UpdateUserUseCase:
    perfil_repo: PerfilRepository = inject.attr(PerfilRepository)
    usuario_repo: UsuariosRepository = inject.attr(UsuariosRepository)
    
    def execute(self, input_dto: MenuInputDto) -> UserMakeOutputDto:

        code = 0
        data = None
        status = 400
        message = ""
        perfil = self.perfil_repo.get_by_id(input_dto.perfil_id)
        user = None
        if perfil is not None:
            usuario_dto = self.usuario_repo.get_by_id(input_dto.usuario_id)
            usuario_dto.setRut(input_dto.rut)
            usuario_dto.setNombre(input_dto.nombre)
            usuario_dto.setEmail(input_dto.email)
            usuario_dto.setPerfilId(input_dto.perfil_id)
            usuario_dto.setPerfilDescripcion(perfil.descripcion)
            usuario_dto.setPassword(input_dto.password)
            user = self.usuario_repo.update(usuario_dto)
            if user is not None:
                code = 1
                status = 200
                message = "Usuario actualizado correctamente"
            else:
                code = 0
                status = 500
                message = "Error al actualizar el usuario"
        else:
            code = 0
            status = 500
            message = "Perfil no encontrado"

        return UserMakeOutputDto(
            code,
            status,
            message,
            user
        )