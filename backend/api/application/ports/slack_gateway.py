from abc import (
    ABCMeta,
    abstractmethod,
)


class SlackGateway(metaclass=ABCMeta):

    @abstractmethod
    def notify_user(self, usuario_id: int, uid: str) -> None:
        pass
