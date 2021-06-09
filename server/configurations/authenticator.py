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
        if re.match(allowed_url, connexion.request.path):
            return

    print('connexxion', connexion)
    print('conexxin request', connexion.request)
    print('conexion request headers', connexion.request.headers)
    x_api_key = connexion.request.headers.get("x-api-key")
    print('ESSE É O X API KEY: ', x_api_key)

    if x_api_key is None:
        raise Unauthorized("Token não passado no header")

