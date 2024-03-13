import re
from app.schemas.base import CustomBaseModel
from pydantic import field_validator


class Category(CustomBaseModel):
    name: str
    slug: str

    @field_validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|[0-9]|-|_)+$', value):
            raise ValueError('Invalid Slug')
        return value


class CategoryOutput(Category):
    id: int

    class Config:
        orm_mode = True
