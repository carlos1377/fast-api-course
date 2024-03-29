from app.schemas.base import CustomBaseModel
from datetime import datetime
from pydantic import field_validator
import re


class User(CustomBaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value

    # @field_validator('password')
    # def validate_password(cls, value):
    #     ...


class TokenData(CustomBaseModel):
    access_token: str
    expires_at: datetime
