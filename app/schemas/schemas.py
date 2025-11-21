from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = "user"


class UserRead(BaseModel):
    id: int
    name: str
    email: str
    role: str
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str

class ActivityCreate(BaseModel):
    user_id: int
    type: str
    value: float
    date: str

class ActivityRead(BaseModel):
    id: int
    user_id: int
    type: str
    value: float
    date: str
    class Config:
        orm_mode = True

class CarbonFootprintRead(BaseModel):
    id: int
    user_id: int
    total: float
    period: str
    class Config:
        orm_mode = True
