from fastapi import APIRouter, Header
from typing import Optional
from app.models.auth import UserRegister, UserLogin, ForgotPasswordRequest
from app.models.response import create_response

router = APIRouter()

# 🧪 Simulated in-memory user store
fake_users = {
    "sample@email.com": {
        "full_name": "Roger",
        "email": "sample@email.com",
        "password": '1234'
    }
}

# 🧪 Simulated token storage (not recommended for real apps)
revoked_tokens = set()


@router.post("/register", tags=["Auth"], summary="Register a new user")
def register(user: UserRegister):
    """
    Register a new user.

    - ❌ If the email is already registered, returns 403
    - ✅ On success, returns user data

    🚧 NOTE: In production, passwords should be hashed and stored securely.
    """
    if user.email in fake_users:
        return create_response("Email already registered", status_code=403)

    # Add user to fake store (in-memory simulation)
    data = {
        "email": user.email,
        "full_name": user.full_name,
        "password": user.password  # ❗️ Don't store plain passwords in real applications
    }
    fake_users[user.email] = data
    return create_response("User registered successfully", data=data, status_code=200)


@router.post("/login", tags=["Auth"], summary="Log in a user")
def login(user: UserLogin):
    """
    Log in with an email and password.

    - ❌ Returns 403 if credentials are invalid
    - ✅ Returns a fake access token on success

    🔐 TODO: Replace with JWT-based authentication.
    """
    stored_user = fake_users.get(user.email)
    if not stored_user or stored_user["password"] != user.password:
        return create_response("Invalid credentials", status_code=403)

    # Simulate returning a token
    data = {
        "access_token": "fake-jwt-token",
        "refresh_token": "fake-refresh-token",
        "token_type": "bearer"
    }
    return create_response("Login successful", data=data, status_code=200)


@router.post("/forgot-password", tags=["Auth"], summary="Request password reset")
def forgot_password(data: ForgotPasswordRequest):
    """
    Initiate a password reset by providing an email.

    - ❌ If email is not found, returns 404
    - ✅ Otherwise, simulates sending a reset link

    📨 TODO: Integrate email sending with a service like SendGrid, Mailgun, etc.
    """
    if data.email not in fake_users:
        return create_response("Email not found", status_code=404)

    return create_response("Password reset sent", status_code=200)


@router.post("/logout", tags=["Auth"], summary="Logout user (invalidate token)")
def logout(authorization: Optional[str] = Header(None)):
    """
    Logs out a user by simulating token invalidation.

    - Requires `Authorization` header with token.
    - Adds token to a blacklist (mock).

    ❗️ In real apps, use token revocation via Redis or JWT blacklist.
    """
    if not authorization:
        return create_response("Missing Authorization header", status_code=401)

    token = authorization.replace("Bearer ", "")
    revoked_tokens.add(token)
    return create_response("Logged out successfully", status_code=200)


@router.post("/refresh-token", tags=["Auth"], summary="Refresh access token")
def refresh_token(authorization: Optional[str] = Header(None)):
    """
    Refreshes the access token using a refresh token.

    - ❌ If refresh token is invalid or revoked, return 401
    - ✅ Returns new access token and token type

    🔐 TODO: Implement secure JWT refresh strategy with expiration handling.
    """
    if not authorization:
        return create_response("Missing Authorization header", status_code=401)

    token = authorization.replace("Bearer ", "")
    if token in revoked_tokens:
        return create_response("Refresh token is revoked", status_code=401)

    # Simulate token refresh
    data = {
        "access_token": "new-fake-access-token",
        "token_type": "bearer"
    }
    return create_response("Token refreshed successfully", data=data, status_code=200)
