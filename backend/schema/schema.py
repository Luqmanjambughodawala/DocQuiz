from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    question_no: int
    question: str
    options: List[str]
    answer: str

class Quiz(BaseModel):
    questions: List[Question]

