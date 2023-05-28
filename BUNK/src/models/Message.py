from pydantic import BaseModel
from enum import Enum
import datetime

class MessageType(Enum):
    USER = "user"
    BOT = "bot"

class Message(BaseModel):
    content: str
    type: MessageType
    timestamp: datetime.datetime = None
    conversationContext: str = None

    def Message(self, content: str, type: MessageType, conversationContext: str = None):
        super().__init__(content=content, type=type, conversationContext=conversationContext)
        self.timestamp = self.timestamp if self.timestamp is not None else datetime.datetime.now()
