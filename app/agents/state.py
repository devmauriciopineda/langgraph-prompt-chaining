from pydantic import BaseModel


class State(BaseModel):
    text: str
    summary: str = None
    translation: str = None
