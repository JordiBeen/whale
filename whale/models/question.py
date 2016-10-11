# encoding: utf-8
import logging

from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship
from .meta import DBSession, Base

log = logging.getLogger(__name__)


class Question(Base):
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer_id = Column(Integer, ForeignKey('answer.id'))
    answer = relationship('Answer', backref='question')

    def __json__(self):
        # set fields here
        fields = ("id",
                  "question"
                  )

        retval = dict((k, getattr(self, k, None)) for k in fields)
        retval['answer'] = self.answer.to_json()
        return retval

    def to_json(self):
        return self.__json__()


def get_question(id_=None):
    q = DBSession.query(Question)
    if id_:
        q = q.filter(Question.id == id_)

    return q.first()


def list_questions():
    q = DBSession.query(Question)
    return q.all()
