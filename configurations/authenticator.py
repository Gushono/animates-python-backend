import re

import connexion
import flask
from flask import g
from werkzeug.exceptions import Unauthorized


def verify_auth():
    g.username = ""

    allowed_urls = [
        "/v1/ui",
        "/v1/ui/",
        "/v1/usuario",
        "/v1/autenticacao",
        "/v1/swagger.json",
    ]

    for allowed_url in allowed_urls:
        if re.fullmatch(allowed_url, connexion.request.path):
            return

    x_auth_token = connexion.request.headers.get("x-auth-token")

    if x_auth_token is None:
        raise Unauthorized()

    flask.g.username = 'zezinho'

    return
