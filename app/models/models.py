from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")  # 'user' ou 'admin'

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    type = Column(String, index=True)
    value = Column(Float)
    date = Column(String)


class CarbonFootprint(Base):
    __tablename__ = "carbon_footprints"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    total = Column(Float)
    period = Column(String)

# Données OpenAQ (qualité de l'air)
class AirQuality(Base):
    __tablename__ = "air_quality"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    location = Column(String)
    parameter = Column(String)
    value = Column(Float)
    unit = Column(String)
    date_utc = Column(String)

# Données Open-Meteo (météo)
class Weather(Base):
    __tablename__ = "weather"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String)
    date_utc = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    wind_speed = Column(Float)
