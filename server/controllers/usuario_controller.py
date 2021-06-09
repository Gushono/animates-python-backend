from typing import Tuple

from server.models.usuario import UsuarioSchema
from server.services import usuario_service


def post_usuario(body: dict) -> Tuple[UsuarioSchema, int]:
    """
    POST -> /usuario

    :param body: UsuarioDTO no SWAGGER

    :return: Retorna um UsuarioSchema
    """
    return usuario_service.criar_usuario(body), 201
