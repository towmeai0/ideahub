from app.core.mongodb import ideas_collection
from bson import ObjectId

async def create_idea(data):
    result = await ideas_collection.insert_one(data)
    return str(result.inserted_id)

async def get_all_ideas():
    ideas = []
    cursor = ideas_collection.find().sort("created_at", -1)
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        ideas.append(doc)
    return ideas

async def upvote_idea(idea_id: str):
    await ideas_collection.update_one(
        {"_id": ObjectId(idea_id)},
        {"$inc": {"votes": 1}}
    )
