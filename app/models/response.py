from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    success: bool = True
    code: int
    message: str
    data: Optional[Any] = None
    
def create_response(message: str, data=None, status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": status_code < 400,
            "code": status_code,
            "message": message,
            "data": data,
        }
    )