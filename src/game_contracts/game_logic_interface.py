from abc import ABCMeta, abstractmethod
from pydantic import BaseModel
from typing import Union

PydanticModelMeta = type(BaseModel)     # works for both v1 and v2

class ABCModelMeta(PydanticModelMeta, ABCMeta):
    """Combine Pydantic’s and ABC’s metaclass logic."""

class GameLogicABC(BaseModel, metaclass=ABCModelMeta):
    @abstractmethod
    def setup_game_state(self, game_state: dict) -> None: ...

    @abstractmethod
    def build_new_game_state(self) -> dict:
        return {}

    @abstractmethod
    def is_game_over(self) -> bool: ...

    @abstractmethod
    def get_current_player(self) -> int: ...

    @abstractmethod
    def get_available_actions(self, player_id: int) -> list[dict[str, str]]: ...

    @abstractmethod
    def apply_action(self, action: str, player: int) -> None: ...

    @abstractmethod
    def report_game_state(self) -> dict[str, str]: ...

    @abstractmethod
    def post_turn_cleanup(self, player_id: int) -> None: ...

    @abstractmethod
    def handle_input(self, input_data: dict) -> None: ...
