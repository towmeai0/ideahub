from fastapi import APIRouter
from app.schemas.user_schema import UserRegister, UserLogin
from app.src.user_collection import register_user, login_user
from app.utils.std_response import success_response, error_response

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(payload: UserRegister):
    try:
        await register_user(payload.email, payload.password)
        return success_response(message="User registered successfully", data={"status": "registered"})
    except ValueError as e:
        return error_response(message="Registration failed", e=e, code=400)
    except Exception as e:
        return error_response(message="Unexpected error occurred", e=e, code=500)

@router.post("/login")
async def login(payload: UserLogin):
    try:
        token = await login_user(payload.email, payload.password)
        return success_response(
            message="Login successful",
            data={"access_token": token, "token_type": "bearer"}
        )
    except ValueError as e:
        return error_response(message="Invalid credentials", e=e, code=401)
    except Exception as e:
        return error_response(message="Unexpected error occurred", e=e, code=500)
