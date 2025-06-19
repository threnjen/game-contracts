from abc import ABC, abstractmethod


class RunnerClientABC(ABC):

    @abstractmethod
    def poll_for_server_response(self) -> dict: ...

    @abstractmethod
    def post_to_server(self, action) -> None: ...

    @abstractmethod
    def get_games_for_player(self, game_configs) -> list: ...

    @abstractmethod
    def setup_new_game(self, game_configs) -> dict: ...

    @abstractmethod
    def initialize_server(self, game_configs) -> dict: ...
