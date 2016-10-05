from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from .routes import setup_routes
from .models.meta import DBSession, Base
from pyramid.session import UnencryptedCookieSessionFactoryConfig


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    Base.metadata.bind = engine
    config = Configurator(settings=settings,
                          session_factory=my_session_factory)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)

    setup_routes(config)
    config.scan()
    return config.make_wsgi_app()
