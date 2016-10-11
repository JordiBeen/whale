# encoding: utf-8
import logging

from sqlalchemy import (Column, Integer, String)
from .meta import DBSession, Base

log = logging.getLogger(__name__)


class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    answer = Column(String)

    def __json__(self):
        # set fields here
        fields = ("id",
                  "answer"
                  )

        retval = dict((k, getattr(self, k, None)) for k in fields)
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
