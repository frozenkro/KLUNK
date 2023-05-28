from pydantic import BaseModel
from .Message import Message

class Interaction(BaseModel):
    proompt: Message
    response: Message | None = None
    conversationContext: str | None = None
