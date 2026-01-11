from fastapi import FastAPI
from app.routes.route import router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Webhook Ingestion Service")
app.include_router(router)

