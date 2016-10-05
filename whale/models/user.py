# encoding: utf-8
import logging

from sqlalchemy import (Column, Integer, String)
from .meta import DBSession, Base

log = logging.getLogger(__name__)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    firstname = Column(String)
    infix = Column(String)
    lastname = Column(String)
    email = Column(String)


def get_user(id_=None):
    q = DBSession.query(User)
    if id_:
        q = q.filter(User.id == id_)

    return q.first()
