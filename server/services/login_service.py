import datetime
from inspect import signature

import connexion
import jwt
from werkzeug.exceptions import Unauthorized

from configurations.enviroment_variables import SECRET_KEY
from server.models.autenticacao import Autenticacao, AutenticacaoSchema
from server.models.usuario import Usuario
from server.repository import login_repository, base_repository
from server.services import util


def token_requerido(func):
    """
    Decorator que verifica em cada chamada se o token é válido
    :param func:
    :return:
    """

    def inner(*args, **kwargs):
        sig = signature(func)
        valida_token(connexion.request.headers.get("x-auth-token"))

        if len(sig.parameters) > 0:
            return func(*args, **kwargs)
        else:
            return func()

    return inner


def valida_token(token):
    auth = login_repository.verifica_token(token)

    if auth is not None:
        if datetime.datetime.utcnow() < auth.expiration_date:
            return

    raise Unauthorized("Token inválido ou expirado")


def autentica_user(autenticacao_dto):
    user = login_repository.verifica_user_and_password(autenticacao_dto["email"],
                                                       autenticacao_dto["senha"])

    if user is not None:
        token = criar_autenticacao(user, autenticacao_dto)
        return util.serialize_entidade(token, AutenticacaoSchema)

    raise Unauthorized("Usuário ou senha invalida")


def criar_autenticacao(user: Usuario, autenticacao_dto: dict):
    expiration_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    token = gerar_token(autenticacao_dto, expiration_date)

    auth = Autenticacao()
    auth.relacao_usuario = user
    auth.token = format_token(token)
    auth.expiration_date = expiration_date

    base_repository.gravar_objeto(auth)

    return auth.token


def gerar_token(autenticacao_dto, expiration_date):
    token = jwt.encode({"email": autenticacao_dto["email"],
                        'expiration_date': str(expiration_date)},
                       SECRET_KEY)

    return token


def format_token(token):
    str_token = str(token)
    formated_token = str_token.replace(str_token[0: 2], '').replace(str_token[-1], '')
    return formated_token
