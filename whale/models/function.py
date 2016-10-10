# encoding: utf-8
import logging

from sqlalchemy import (Column, Integer, String)
from .meta import DBSession, Base

log = logging.getLogger(__name__)


class Function(Base):
    __tablename__ = "function"

    id = Column(Integer, primary_key=True)
    function = Column(String)

    def __json__(self):
        # set fields here
        fields = ("id",
                  "function"
                  )

        retval = dict((k, getattr(self, k, None)) for k in fields)
        return retval

    def to_json(self):
        return self.__json__()


def get_function(id_=None):
    q = DBSession.query(Function)
    if id_:
        q = q.filter(Function.id == id_)

    return q.first()


def list_functions():
    q = DBSession.query(Function)
    return q.all()
