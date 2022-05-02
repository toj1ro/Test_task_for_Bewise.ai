from typing import Optional

from pydantic import BaseModel


class QuestionsSchema(BaseModel):
    question_text: Optional[str] = None
    answer_text: Optional[str] = None


class RequestQuestionsSchema(BaseModel):
    questions_num: Optional[int] = None
