from fastapi import FastAPI
from app.routers.events import router as events_router
from app.routers.users import router as users_router
from app.database.session import Base, engine

app = FastAPI(title="Мероприятия & Пользователи")
Base.metadata.create_all(bind=engine)


app.include_router(events_router)
app.include_router(users_router)