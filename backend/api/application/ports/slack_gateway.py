from abc import (
    ABCMeta,
    abstractmethod,
)

class SlackGateway(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def notify_user(self, email: str, msg: str) -> bool:
        pass
