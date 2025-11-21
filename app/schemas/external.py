from pydantic import BaseModel
from typing import Optional
# ...existing code...

class AirQualityCreate(BaseModel):
    city: str
    location: str
    parameter: str
    value: float
    unit: str
    date_utc: str

class AirQualityRead(BaseModel):
    id: int
    city: str
    location: str
    parameter: str
    value: float
    unit: str
    date_utc: str
    class Config:
        orm_mode = True

class WeatherCreate(BaseModel):
    city: str
    date_utc: str
    temperature: float
    humidity: float
    wind_speed: float

class WeatherRead(BaseModel):
    id: int
    city: str
    date_utc: str
    temperature: float
    humidity: float
    wind_speed: float
    class Config:
        orm_mode = True
