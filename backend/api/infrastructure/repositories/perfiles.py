from abc import (
    ABCMeta,
    abstractmethod
)
from api.application.repositories import PerfilRepository
from api.domain.entities import Perfil
from datetime import datetime
import typing

class DjangoORMPerfilRepository(PerfilRepository):

    def get_by_id(self, id_perfil: int) -> typing.List[Perfil]:
        from api.models import (
            Perfil as PerfilModel
        )
        try:
            perfil_model = PerfilModel.objects.get(id = id_perfil)
            return Perfil(id = perfil_model.id, descripcion = perfil_model.descripcion)
        except Exception as e:
            return None