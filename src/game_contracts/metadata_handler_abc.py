from abc import ABC, abstractmethod


class GameMetadataHandlerABC(ABC):

    @abstractmethod
    def get_games_by_player(self, player_id: str) -> dict: ...

    @abstractmethod
    def setup_new_game_id(self, game_configs: dict) -> dict: ...

    @abstractmethod
    def initialize_game(self, game_id: str) -> None: ...

    @abstractmethod
    def get_game_state(self, game_id: str) -> dict: ...
