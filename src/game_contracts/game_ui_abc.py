from abc import ABC, abstractmethod


class GameUI(ABC):

    @abstractmethod
    async def start(self): ...

    @abstractmethod
    def send_action_to_server(self, payload) -> None: ...

    @abstractmethod
    async def wait_for_server_response(self) -> dict: ...

    @abstractmethod
    async def background_poll_loop(self) -> None: ...

    @abstractmethod
    def ui_side_cleanup(self) -> bool: ...

    @abstractmethod
    def handle_message(self, message) -> bool: ...
