from abc import ABC, abstractmethod
from typing import Any


class RunnerServerABC(ABC):
    @abstractmethod
    def poll_for_message_from_client(self) -> dict:
        """Blocking or polling wait until a message is received from a client"""
        pass

    @abstractmethod
    def push_message_to_client(self, payload: dict) -> None:
        """Send a message to the specified client (they will poll for it)"""
        pass

    @abstractmethod
    def get_game_state(self, game_id: str) -> list:
        """Retrieve the current game state for the specified game ID"""
        pass
