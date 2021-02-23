from typing import Optional



class Status:
    def __init__(self, id: Optional[int], descripcion: str) -> None:
        self._id = id
        self._descripcion = descripcion
    
    @property
    def id(self):
        return self._id

    @property
    def descripcion(self):
        return self._descripcion

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
