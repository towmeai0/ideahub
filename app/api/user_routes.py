from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRegister, UserLogin
from app.src import user_collection

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(payload: UserRegister):
    try:
        await user_collection.register_user(payload.email, payload.password)
        return {"status": "registered"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(payload: UserLogin):
    try:
        token = await user_collection.login_user(payload.email, payload.password)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid credentials")
