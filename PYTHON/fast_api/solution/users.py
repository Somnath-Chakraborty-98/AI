import uuid
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from fastapi_users.db import SQLAlchemyUserDatabase
from db import User, get_user_db

SECRET = "SOUSKE_AIZEN_990#@"

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    
    async def on_after_register(self, user, request = None):
        print(f"User {user.id} has registered")
        
    
async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
    
bearer_transpost = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy():
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name = "jwt",
    transport = bearer_transpost,
    get_strategy = get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager= get_user_manager, auth_backends=[auth_backend])
current_active_user = fastapi_users.current_user(active=True)