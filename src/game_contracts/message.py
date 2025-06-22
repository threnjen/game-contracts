import hashlib
import json
from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field, computed_field


class MessageSource(str, Enum):
    CLIENT = "client"
    SERVER = "server"


class MessageEnvelope(BaseModel):
    game_id: str
    client_id: str
    source: MessageSource
    seq: int = 0
    signature: str | None = None
    payload: dict


class ServerMessage(MessageEnvelope):
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    source: MessageSource = MessageSource.SERVER

    @computed_field
    @property
    def message_id(self) -> str:
        raw = f"{self.client_id}-{self.timestamp.isoformat()}-{json.dumps(self.payload, sort_keys=True)}"
        return hashlib.sha256(raw.encode()).hexdigest()
