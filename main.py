from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/questions/{question_id}")
def get_questions(question_id: int, db: Session = Depends(get_db)):
    db_question = crud.get_question(db, question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question with this id not found")
    return db_question


@app.post("/questions")
def create_questions(questions: schemas.RequestQuestionsSchema, db: Session = Depends(get_db)):
    q = crud.jservice_request(questions.questions_num)
    for question in q:
        crud.add_question(db, question)
    return {"message": "OK"}


@app.put("/questions/{question_id}")
def update_questions(question_id: int, questions: schemas.QuestionsSchema, db: Session = Depends(get_db)):
    db_question = crud.get_question(db=db, id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="Question with this id not found")
    crud.update_question(db_question=db_question, db=db, question=questions)
    return {"message": "OK"}

@app.delete("/questions/{question_id}")
def delete_questions(question_id: int, db: Session = Depends(get_db)):
    if not crud.delete_question(db=db, question_id=question_id):
        raise HTTPException(status_code=404, detail="Question with this id not found")
    else:
        return {"message": "OK"}
