from app.core.mongodb import db
from app.utils.security import hash_password, verify_password, create_access_token

async def register_user(email: str, password: str):
    existing = await db.users.find_one({"email": email})
    if existing:
        raise ValueError("User already exists")

    hashed = hash_password(password)
    await db.users.insert_one({
        "email": email,
        "password": hashed
    })


async def login_user(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if not user:
        raise ValueError("Invalid credentials")

    if not verify_password(password, user["password"]):
        raise ValueError("Invalid credentials")

    token = create_access_token({
        "user_id": str(user["_id"]),
        "email": user["email"]
    })
    return token
