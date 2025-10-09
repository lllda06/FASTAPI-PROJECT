from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, events
from app.models import user, event

# Создаём таблицы, если их нет
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI SQLite Example")

# Подключаем роутеры
app.include_router(users.router)
app.include_router(events.router)


@app.get("/")
def root():
    return {"message": "FastAPI с событиями и пользователями!"}
