from pydantic import BaseModel


class State(BaseModel):
    text: str
    topic: str = None
    summary: str = None
    translation: str = None
    success: bool = None
