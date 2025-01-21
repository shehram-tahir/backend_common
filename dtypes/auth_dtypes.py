from typing import Dict, List, TypeVar, Generic, Optional, Any
from pydantic import BaseModel

# Base classes
class ReqUserId(BaseModel):
    user_id: str

class ReqAuth(BaseModel):
    email: str
    password: str

# Derived classes
class ReqCreateFirebaseUser(ReqAuth):
    username: str

class ReqCreateUserProfile(ReqCreateFirebaseUser, ReqUserId):
    pass

class ReqUserLogin(ReqAuth):
    pass

class ReqUserProfile(ReqUserId):
    pass

class ReqResetPassword(BaseModel):
    email: str

class ReqConfirmReset(BaseModel):
    oob_code: str
    new_password: str

class ReqChangePassword(ReqUserId, ReqAuth):
    new_password: str

class ReqChangeEmail(ReqUserId):
    current_email: str
    new_email: str
    password: str

class ReqRefreshToken(BaseModel):
    grant_type: str
    refresh_token: str