from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schemas import CarbonFootprintRead
from app.models.models import CarbonFootprint, Activity
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/carbon_footprint/{user_id}", response_model=CarbonFootprintRead)
def calculate_carbon_footprint(user_id: int, db: Session = Depends(get_db)):
    activities = db.query(Activity).filter(Activity.user_id == user_id).all()
    if not activities:
        raise HTTPException(status_code=404, detail="No activities found for user")
    # Exemple de calcul simple : somme des valeurs
    total = sum(a.value for a in activities)
    carbon_fp = CarbonFootprint(user_id=user_id, total=total, period="all")
    db.add(carbon_fp)
    db.commit()
    db.refresh(carbon_fp)
    return carbon_fp
