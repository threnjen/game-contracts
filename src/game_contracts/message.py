from pydantic import BaseModel, computed_field
from enum import Enum
from datetime import datetime, timezone


class MessageSource(str, Enum):
    CLIENT = "client"
    SERVER = "server"


class Message(BaseModel):
    client_id: str
    source: MessageSource
    payload: dict


class ServerMessage(Message):
    timestamp: datetime = datetime.now(timezone.utc)
    source: MessageSource = MessageSource.SERVER

    @computed_field
    @property
    def message_id(self) -> int:
        return hash(f"{self.client_id}-{self.timestamp.isoformat()}-{self.payload}")
