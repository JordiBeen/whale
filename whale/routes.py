def setup_routes(config):
    # Home
    config.add_route('home', '/')

    # User
    config.add_route('users.list', '/users',
                     request_method='GET')

    # Question
    config.add_route('question.post', '/question',
                     request_method='POST')
