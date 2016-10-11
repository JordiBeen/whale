import logging

from pyramid.view import view_config
from pyramid import httpexceptions

log = logging.getLogger(__name__)


@view_config(route_name='question.post', permission='public',
             renderer="json")
def question_post(request):
    settings = request.registry.settings
    request_data = request.json_body

    if request_data.get('token') != settings.get('whale.token'):
        return httpexceptions.HTTPForbidden()

    return_data = {"ja": "het werkt"}
    return {
        'data': return_data
    }
