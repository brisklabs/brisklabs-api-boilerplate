from pydantic import BaseModel


class UserUpdate(BaseModel):
    full_name: str


class UserResponse(BaseModel):
    email: str
    full_name: str
