import logging

from pyramid.view import view_config

from ..models.user import list_users

log = logging.getLogger(__name__)


@view_config(route_name='users.list', permission='public',
             renderer="json")
def users_list(request):
    users = list_users()

    log.info("{} Start of log: '{}' {}".format("-" * 40, "New request:", "-" * 40))
    log.info("{} Start of log: '{}' {}".format("-" * 40, "USER", "-" * 40))
    log.info(request)
    log.info("{} End of log: '{}' {}".format("-" * 40, "End of request", "-" * 40))

    return {
        'users': [user.to_json() for user in users]
    }
