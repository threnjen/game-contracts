from abc import ABC, abstractmethod
from typing import Any


class RunnerServerABC(ABC):
    @abstractmethod
    async def poll_for_input(self, player_id: str) -> Any: ...

    @abstractmethod
    async def receive_action(self, player_id: str, request) -> Any: ...

    @abstractmethod
    async def get_actions(self, player_id: str) -> Any: ...

    @abstractmethod
    async def push_response(self, player_id: str, request) -> Any: ...
