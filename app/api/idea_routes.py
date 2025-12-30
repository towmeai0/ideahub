from fastapi import APIRouter
from app.schemas.idea_schema import IdeaCreate
from app.src import idea_collection

router = APIRouter(tags=["Ideas"])

@router.post("/ideas/create")
async def create_idea(payload: IdeaCreate):
    idea_id = await idea_collection.create_idea(payload.dict())
    return {"id": idea_id}

@router.get("/list/ideas")
async def list_ideas():
    return await idea_collection.get_all_ideas()

@router.post("/{idea_id}/upvote")
async def upvote(idea_id: str):
    await idea_collection.upvote_idea(idea_id)
    return {"status": "upvoted"}
