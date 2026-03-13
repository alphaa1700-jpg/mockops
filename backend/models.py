from sqlalchemy import Column, Integer, String
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    level = Column(String)


class InterviewSession(Base):
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    score = Column(Integer, default=0)
    current_question = Column(Integer, default=0)
