from pydantic import BaseModel


class GameState(BaseModel):
    players: dict
    targetables: dict
    cards: dict
