from server.services import login_service


def post_autenticacao(body):
    """
    POST -> /autenticar

    :param body: UsuarioVO no SWAGGER

    :return: AutenticacaoSchema
    """

    return login_service.autentica_user(body), 200
