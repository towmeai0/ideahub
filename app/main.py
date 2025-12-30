from fastapi import FastAPI
from app.api import idea_routes, user_routes
from zoneinfo import ZoneInfo

_IST = ZoneInfo("Asia/Kolkata")

app = FastAPI(
    title="APIs",
    description="Apiiii",
    version="1.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redocs"
)


app.include_router(idea_routes.router, prefix="/api")
app.include_router(user_routes.router, prefix="/api")


@app.get("/")
def read_root():
    return {"message": "API is live!"}
