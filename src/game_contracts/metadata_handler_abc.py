from abc import ABC, abstractmethod


class GameMetadataHandlerABC(ABC):

    @abstractmethod
    def get_games_by_player(self, player_id: str) -> dict: ...

    @abstractmethod
    def setup_new_game_id(self, game_configs: dict) -> dict: ...

    @abstractmethod
    def get_game_state(self, game_id: str) -> dict: ...

    @abstractmethod
    def update_game_state(self, game_id: str, game_state: dict) -> None: ...

    @abstractmethod
    def preprocess_action(self, action: str, player_id: str): ...

    @abstractmethod
    def filter_state_for_player(self, state: str, player_id: str): ...
