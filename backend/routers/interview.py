from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import InterviewSession, Question
import uuid
import random

router = APIRouter()

@router.post("/start")
def start_interview(name: str, db: Session = Depends(get_db)):
    session_id = str(uuid.uuid4())
    new_session = InterviewSession(id=session_id, name=name)
    db.add(new_session)
    db.commit()
    return {"session_id": session_id}


@router.get("/next/{session_id}")
def next_question(session_id: str, db: Session = Depends(get_db)):
    session = db.query(InterviewSession).filter(InterviewSession.id == session_id).first()
    total = db.query(Question).count()

    if session.current_question >= total:
        return {"message": "Finished", "score": session.score}

    question = db.query(Question).offset(random.randint(0, total - 1)).first()
    return question


@router.post("/submit/{session_id}")
def submit(session_id: str, answer: str, db: Session = Depends(get_db)):
    session = db.query(InterviewSession).filter(InterviewSession.id == session_id).first()
    score = len(answer) % 10
    session.score += score
    session.current_question += 1
    db.commit()
    return {"score": session.score}
