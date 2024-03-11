from typing import Optional
from pydantic import BaseModel, constr, validator
from datetime import date


class BlogPost(BaseModel):
    title: constr(min_length=5, max_length=100)
    content: constr(min_length=10)
    author: str
    publication_date: date
    tags: Optional[list[str]]

    @validator("tags", pre=True, each_item=True)
    def validate_tags(cls, tag):
        if not tag.isalpha():
            raise ValueError("Tags must contain only alphabetic characters")
        return tag


class UpdateBlogPost(BaseModel):
    title: constr(min_length=5, max_length=100) = None
    content: constr(min_length=10) = None
    author: str = None
    publication_date: date = None
    tags: Optional[list[str]] = None

    @validator("tags", pre=True, each_item=True)
    def validate_tags(cls, tag):
        if not tag.isalpha():
            raise ValueError("Tags must contain only alphabetic characters")
        return tag
