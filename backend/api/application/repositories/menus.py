from abc import (
    ABCMeta,
    abstractmethod
)

from api.domain.entities import Menu
from datetime import datetime
import typing

class MenusRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> typing.List[Menu]:
        pass

    @abstractmethod
    def get_by_id(self, menu_id: int) -> Menu:
        pass

    @abstractmethod
    def get_by_id_list(self, menu_id: typing.List[int]) -> typing.List[Menu]:
        pass

    @abstractmethod
    def get_by_date(self, date: datetime ) -> typing.List[Menu]:
        pass
    @abstractmethod
    def get_by_date_status(self, date: datetime, get_by_date_status: int ) -> typing.List[Menu]:
        pass
    
    @abstractmethod
    def update(self, menu: Menu) -> Menu:
        pass
    
    @abstractmethod
    def save(self, menu: Menu) -> Menu: 
        pass

    def delete(self, menu_id: int) -> bool:
        pass


