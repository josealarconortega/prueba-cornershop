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
    rut: str
    nombre: int
    email: str
    perfil_id: str
    password: str


@dataclass
class UserMakeOutputDto:
    code: int
    status: int
    message: str
    data: Usuario

class MakeNewUserUseCase:
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
            i = 0
            user = self.usuario_repo.save(Usuario(None, input_dto.rut, input_dto.nombre, input_dto.email, date.today(), uuid.uuid4(), input_dto.perfil_id, input_dto.password ))
            if user is not None:
                code = 1
                status = 200
                message = "Usuario registrado correctamente"
            else:
                code = 0
                status = 500
                message = "Error al registrar el usuario"
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