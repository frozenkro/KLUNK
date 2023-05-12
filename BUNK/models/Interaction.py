from pydantic import BaseModel

class Interaction(BaseModel):
    proompt: str
    response: str | None = None
    conversationContext: str | None = None
