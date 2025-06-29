from pydantic import BaseModel
from abc import abstractmethod


class GameState(BaseModel):
    players: dict
    targetables: dict
    cards: dict


class Command(BaseModel):
    source: str
    target: str

    @abstractmethod
    def execute(self, state):
        pass
