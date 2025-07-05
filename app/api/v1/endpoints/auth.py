from fastapi import APIRouter, HTTPException
from app.models.auth import UserRegister, UserLogin, ForgotPasswordRequest

router = APIRouter()


# Simulated in-memory user store
fake_users = {}


@router.post("/register", tags=["Auth"])
def register(user: UserRegister):
    if user.email in fake_users:
        raise HTTPException(status_code=400, detail="Email already registered")

    fake_users[user.email] = {
        "full_name": user.full_name,
        "password": user.password  # NOTE: in real app, hash this!
    }

    return {"message": "User registered successfully"}


@router.post("/login", tags=["Auth"])
def login(user: UserLogin):
    stored_user = fake_users.get(user.email)
    if not stored_user or stored_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Simulate returning a token
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}


@router.post("/forgot-password", tags=["Auth"])
def forgot_password(data: ForgotPasswordRequest):
    if data.email not in fake_users:
        raise HTTPException(status_code=404, detail="Email not found")

    # Simulate sending reset link
    return {"message": f"Password reset link sent to {data.email}"}
