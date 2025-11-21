from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.models.models import AirQuality, Weather
from app.schemas.external import AirQualityCreate, AirQualityRead, WeatherCreate, WeatherRead
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint pour ajouter une mesure OpenAQ
@router.post("/air_quality/", response_model=AirQualityRead)
def add_air_quality(data: AirQualityCreate, db: Session = Depends(get_db)):
    aq = AirQuality(**data.dict())
    db.add(aq)
    db.commit()
    db.refresh(aq)
    return aq

# Endpoint pour ajouter une mesure météo Open-Meteo
@router.post("/weather/", response_model=WeatherRead)
def add_weather(data: WeatherCreate, db: Session = Depends(get_db)):
    w = Weather(**data.dict())
    db.add(w)
    db.commit()
    db.refresh(w)
    return w

# Endpoint pour lister les mesures OpenAQ
@router.get("/air_quality/", response_model=list[AirQualityRead])
def list_air_quality(db: Session = Depends(get_db)):
    return db.query(AirQuality).all()


# Endpoint pour lister les mesures météo
@router.get("/weather/", response_model=list[WeatherRead])
def list_weather(db: Session = Depends(get_db)):
    return db.query(Weather).all()

# Endpoint d'upload CSV pour air_quality
import csv
@router.post("/air_quality/upload_csv/")
async def upload_air_quality_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    contents = await file.read()
    decoded = contents.decode("utf-8").splitlines()
    reader = csv.DictReader(decoded)
    count = 0
    for row in reader:
        aq = AirQuality(
            city=row.get("city", ""),
            location=row.get("location", ""),
            parameter=row.get("parameter", ""),
            value=float(row.get("value", 0)),
            unit=row.get("unit", ""),
            date_utc=row.get("date_utc", "")
        )
        db.add(aq)
        count += 1
    db.commit()
    return {"imported": count}
