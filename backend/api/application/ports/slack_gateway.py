from abc import (
    ABCMeta,
    abstractmethod,
)

class SlackGateway(metaclass=ABCMeta):

    @abstractmethod
    def notify_user(self, email: str, msg: str) -> None:
        pass
