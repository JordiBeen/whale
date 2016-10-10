# encoding: utf-8
import logging

from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.orm import relationship
from .meta import DBSession, Base

log = logging.getLogger(__name__)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    answer = Column(String)
    function_id = Column(Integer, ForeignKey('function.id'))
    function = relationship('Function', backref='answer')

    def __json__(self):
        # set fields here
        fields = ("id",
                  "answer"
                  )

        retval = dict((k, getattr(self, k, None)) for k in fields)
        retval['function'] = self.answer.to_json()
        return retval

    def to_json(self):
        return self.__json__()


def get_answer(id_=None):
    q = DBSession.query(Answer)
    if id_:
        q = q.filter(Answer.id == id_)

    return q.first()


def list_answers():
    q = DBSession.query(Answer)
    return q.all()
