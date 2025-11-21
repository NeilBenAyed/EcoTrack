from fastapi import FastAPI



from app.routes.users import router as users_router
from app.routes.activities import router as activities_router
from app.routes.carbon import router as carbon_router
from app.routes.external import router as external_router

app = FastAPI()


app.include_router(users_router)
app.include_router(activities_router)
app.include_router(carbon_router)
app.include_router(external_router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur EcoTrack API"}
