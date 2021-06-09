import traceback
from pprint import pformat
from venv import logger

import connexion


def token_info(token):
    try:
        token = verfica_token_eh_valido(token)

        if not token:
            return None

        return {
           'usuario': 'zezinho'
        }
    except Exception as ex:
        trace = traceback.format_exc()
        msg = f"Not expected error {ex}, {trace}"
        print(msg)
        return msg


def before_request():
    try:
        logger.info(f"request url: {pformat(connexion.request.base_url)} - {connexion.request.method}")
        logger.info(f"request headers: {pformat(connexion.request.headers)}")
        logger.info(f"request params: {pformat(connexion.request.args)}")
        logger.info(f"request body: {pformat(connexion.request.data)}")
    except Exception as ex:
        logger.warning(f"Erro ao logar request. Continuando fluxo da aplicação. Erro: [{ex}].")


def verfica_token_eh_valido(token):
    return True if token else False
