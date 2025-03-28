from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=150)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=150)
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=6)
    discord_username: Optional[str] = None
    phone_number: Optional[str] = None
    instagram_username: Optional[str] = None
    kakaotalk_id: Optional[str] = None


class UserResponse(UserBase):
    id: int
    discord_username: Optional[str] = None
    phone_number: Optional[str] = None
    instagram_username: Optional[str] = None
    kakaotalk_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
