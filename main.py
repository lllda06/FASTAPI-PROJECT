from fastapi import FastAPI
from app.database.db_connection import Base, engine
from app.routers import users, events
from depends import get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="События, подписки и пользователи!")

app.include_router(users.router)
app.include_router(events.router)

@app.get("/")
def root():
    return {"message": "FastAPI c событиями, подписками на них и пользователями по интересам!"}
