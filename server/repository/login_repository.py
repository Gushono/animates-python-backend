import base64

from server import db
from server.models.autenticacao import Autenticacao
from server.models.usuario import Usuario


def verifica_user_and_password(email, senha):
    utf8_password = senha.encode("utf-8")
    encoded_password_str = str(base64.b64encode(utf8_password))
    formated_password = encoded_password_str.replace(encoded_password_str[0: 2], '').replace(encoded_password_str[-1],
                                                                                             '')

    return db.session.query(Usuario). \
        filter(Usuario.email == email). \
        filter(Usuario.senha == formated_password).first()


def verifica_token(token) -> Autenticacao:
    return db.session.query(Autenticacao).filter(Autenticacao.token == token).first()


def verifica_usuario_logado_por_token(token) -> Usuario:
    return db.session.query(Usuario).join(Autenticacao). \
        filter(Autenticacao.token == token).first()
