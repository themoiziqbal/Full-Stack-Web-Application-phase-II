from fastapi import FastAPI
from .api.routes import tasks
from .db import init_db

app = FastAPI(title="Evolution of Todo API")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(tasks.router, prefix="/api")

@app.get("/")
def health_check():
    return {"status": "ok", "phase": 2}
