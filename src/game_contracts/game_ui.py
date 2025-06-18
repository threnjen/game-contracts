from abc import ABC, abstractmethod


class GameUI(ABC):

    @abstractmethod
    async def start(self): ...

    @abstractmethod
    def send_action_to_server(self, payload): ...

    @abstractmethod
    async def wait_for_server_response(self, game_state): ...

    @abstractmethod
    async def background_poll_loop(self, game_state): ...
