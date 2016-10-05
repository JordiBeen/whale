import logging

from pyramid.view import view_config

from ..models.user import get_user

log = logging.getLogger(__name__)


@view_config(route_name='home', permission='public',
             renderer="whale:templates/index.mako")
def home_view(request):
    user = get_user(id_=1)

    return {
        'user': user
    }
