from fastapi.responses import JSONResponse
from typing import Optional, Any

def error_response(message: str, e: Optional[Exception] = None, code: int = 500) -> JSONResponse:
    return JSONResponse(
        status_code=code,
        content={
            "status": "error",
            "code": code,
            "message": message,
            "data": {"detail": str(e)} if e else {}
        },
    )

def success_response(message: str, data: Optional[Any] = None, code: int = 200) -> JSONResponse:
    return JSONResponse(
        status_code=code,
        content={
            "status": "success",
            "code": code,
            "message": message,
            "data": data or {}
        },
    )

