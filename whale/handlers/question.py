import logging

from pyramid.view import view_config
from pyramid import httpexceptions

log = logging.getLogger(__name__)


@view_config(route_name='question.post', permission='public',
             renderer="json")
def question_post(request):
    settings = request.registry.settings
    request_data = request.json_body

    message = ''
    token = ''
    answer_to = ''

    return_data = {}
    return_data['status'] = 'error'
    return_data['answer'] = 'Sorry, I do not understand'

    log.info("{} Start of log: '{}' {}".format("-" * 40, "request_data", "-" * 40))
    log.info(request_data)
    log.info("{} End of log: '{}' {}".format("-" * 40, "request_data", "-" * 40))

    if 'message' in request_data:
        message = request_data.get('message')
    else:
        return_data['answer'] = 'Please specify a message'

    if 'answer_to' in request_data:
        answer_to = request_data.get('answer_to')

    if 'token' in request_data:
        token = request_data.get('token')

    if token != settings.get('whale.token'):
        return httpexceptions.HTTPForbidden()

    return_data['status'] = 'OK'

    # User asking to vibrate
    if 'vibrate' in message:
        return_data['answer'] = 'Okay, how long should I vibrate?'

    # User answers to a question asked
    if answer_to:
        # User is answering how long to vibrate
        if all(x in answer_to for x in ['how', 'long', 'vibrate']):
            if string_has_number(message):
                length = get_number_from_string(message)
                if 'second' in message:
                    length = length
                if 'minute' in message:
                    length = length * 60
                if 'hour' in message:
                    length = length * 60 * 60
                return_data['answer'] = 'Going to vibrate, enjoy!'
                return_data['function'] = {}
                return_data['function']['name'] = 'vibrate'
                return_data['function']['length'] = length

    return {
        'data': return_data
    }


def get_number_from_string(string):
    return [int(s) for s in string.split() if s.isdigit()][0]


def string_has_number(string):
    return any(char.isdigit() for char in string)
