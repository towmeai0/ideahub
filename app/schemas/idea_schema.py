from pydantic import BaseModel
from typing import List

class IdeaCreate(BaseModel):
    title: str
    description: str
    tags: List[str] = []

class IdeaResponse(IdeaCreate):
    id: str
    votes: int
