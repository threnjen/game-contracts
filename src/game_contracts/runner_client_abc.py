from abc import ABC, abstractmethod


class RunnerClientABC(ABC):

    @abstractmethod
    def poll_for_server_response(self) -> dict: ...

    @abstractmethod
    def post_to_server(self, game_id: str, client_id: str, payload: dict) -> None: ...

    @abstractmethod
    def get_games_for_player(self, game_configs: dict) -> dict: ...

    @abstractmethod
    def setup_new_game(self, game_configs: dict) -> dict: ...

    @abstractmethod
    def initialize_server(self, params: dict) -> bool: ...
