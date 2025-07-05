from fastapi import APIRouter, Header
from typing import Optional
from app.models.response import create_response
from app.models.user import UserUpdate

router = APIRouter()

# 🧪 Fake token-to-user mapping
token_user_map = {
    "fake-jwt-token": {
        "email": "sample@email.com",
        "full_name": "Roger"
    },
    "new-fake-access-token": {
        "email": "sample@email.com",
        "full_name": "Roger"
    }
}

def get_user_from_token(authorization: Optional[str]):
    """Simulated interceptor to extract and verify user from token."""
    if not authorization:
        return None
    
    token = authorization.replace("Bearer ", "")
    return token_user_map.get(token)

@router.get("/user", tags=["User"], summary="Get current user")
def get_user(authorization: Optional[str] = Header(None)):
    """
    Get user details from a valid Bearer token.
    """
    user = get_user_from_token(authorization)
    if not user:
        return create_response("Unauthorized access", status_code=401)
    
    return create_response("User fetched successfully", data=user)

@router.put("/user", tags=["User"], summary="Update current user")
def update_user(update: UserUpdate, authorization: Optional[str] = Header(None)):
    """
    Update the user's information.
    """
    token = authorization.replace("Bearer ", "") if authorization else ""
    user = get_user_from_token(authorization)
    if not user:
        return create_response("Unauthorized access", status_code=401)

    # Simulate update
    user["full_name"] = update.full_name
    token_user_map[token]["full_name"] = update.full_name

    return create_response("User updated successfully", data=user)
