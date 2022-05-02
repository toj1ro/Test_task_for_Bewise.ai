import datetime

from sqlalchemy import Column, Integer, Text, DateTime

from db import Base


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    external_id = Column(Integer, index=True)
    question_text = Column(Text)
    answer_text = Column(Text)
    create_data = Column(DateTime, default=datetime.datetime.utcnow())
