from abc import ABCMeta, abstractmethod
from pydantic import BaseModel
from typing import Union

PydanticModelMeta = type(BaseModel)  # works for both v1 and v2


class ABCModelMeta(PydanticModelMeta, ABCMeta):
    """Combine Pydantic’s and ABC’s metaclass logic."""


class GameLogicABC(BaseModel, metaclass=ABCModelMeta):
    @abstractmethod
    def is_game_over(self) -> bool: ...

    """Check if the game is over.
    The method returns True if the game is over, otherwise False."""

    @abstractmethod
    def parse_client_message(self, input_data: dict) -> dict: ...

    """Handle input data for the game logic.
    The method processes the input data and returns the output data.
    The engine 
    Args:
        input_data (dict): Input data for the game logic.
        Returns:
        dict: Output data after processing the input."""

    @abstractmethod
    def get_game_state(self) -> dict:
        """Get the current state of the game.
        Returns:
            dict: The current state of the game.
        """
        return {}
