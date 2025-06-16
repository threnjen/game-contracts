from abc import ABC, abstractmethod


class GameUI(ABC):

    @abstractmethod
    def send_action_to_server(self, actions): ...

    @abstractmethod
    def wait_for_server_response(self): ...
