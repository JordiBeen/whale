import os
import logging
import sys
import transaction

from sqlalchemy import engine_from_config
from ..lib.security import hash_password

from pyramid.paster import (
    get_appsettings,
    setup_logging)

from ..models.meta import DBSession, Base
from ..models import persist
from ..models.user import User, get_user # noqa
from ..models.question import Question # noqa
from ..models.answer import Answer # noqa
from ..models.function import Function # noqa


log = logging.getLogger(__name__)


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri>\n'
          '(example: "%s template.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)
    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)

    with transaction.manager:
        u = get_user(id_=1)
        if not u:
            u = User()
            u.username = "whale"
            u.firstname = "admin"
            u.infix = "of"
            u.lastname = "whale"

            u.email = 'jordibeen@labela.nl'
            u.password = hash_password("password")

            persist(u)

    print("Database initialisation completed.")
