import requests
from sqlalchemy.orm import Session

import models
import schemas


def jservice_request(count: int):
    r = requests.get(f'https://jservice.io/api/random?count={count}')
    return r.json()


def get_question(db: Session, id: int):
    return db.query(models.Questions).filter(models.Questions.id == id).first()


def get_question_by_external_id(db: Session, external_id: int):
    return db.query(models.Questions).filter(models.Questions.external_id == external_id).first()


def create_question(db: Session, question):
    db_question = models.Questions(external_id=question["id"],
                                   question_text=question["question"],
                                   answer_text=question["answer"])
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def add_question(db: Session, q):
    question = get_question_by_external_id(db, q["id"])
    while question is not None:
        q = jservice_request(1)
        question = get_question_by_external_id(db, q["id"])
    create_question(db, q)


def update_question(db_question, db: Session, question: schemas.QuestionsSchema):
    question_data = question.dict(exclude_unset=True)
    for key, value in question_data.items():
        setattr(db_question, key, value)
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return question_data


def delete_question(db: Session, question_id: int):
    db_question = db.query(models.Questions).filter(models.Questions.id == question_id).delete()
    db.commit()
    return db_question
