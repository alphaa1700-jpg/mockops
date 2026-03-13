from fastapi import FastAPI
from database import engine, Base
from routers import interview, question
from prometheus_fastapi_instrumentator import Instrumentator
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.include_router(interview.router)
app.include_router(question.router)

@app.get("/")
def home():
    return {"message": "MockOps Clean Architecture Running"}

@app.get("/health")
def health():
    return {"status": "ok"}
