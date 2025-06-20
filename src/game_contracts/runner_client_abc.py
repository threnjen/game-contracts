from abc import ABC, abstractmethod


class RunnerClientABC(ABC):

    @abstractmethod
    def poll_for_server_response(self) -> dict: ...

    @abstractmethod
    def post_to_server(self, payload) -> None: ...

    @abstractmethod
    def get_games_for_player(self, game_configs) -> dict: ...

    @abstractmethod
    def setup_new_game(self, game_configs) -> dict: ...

    @abstractmethod
    def initialize_server(self, params) -> bool: ...
