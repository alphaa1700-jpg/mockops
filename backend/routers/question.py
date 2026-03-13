from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Question

router = APIRouter()

@router.post("/add-question")
def add_question(question: str, level: str, db: Session = Depends(get_db)):
    new_q = Question(question=question, level=level)
    db.add(new_q)
    db.commit()
    return {"message": "Question Added"}
