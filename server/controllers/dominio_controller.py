from typing import Tuple

from server.controllers import util
from server.models.dominio import DominioSchema
from server.services import dominio_service


def get_listar_dominios() -> Tuple[DominioSchema, int]:
    """
    GET -> /dominios

    :param: pagina: Número da página que deseja mostrar a listagem
    :param: tp_dominio: Nome do tipo do domínio
    :param: nm_dominio: Nome do domínio

    :return: Retorna uma lista de DominioSchema
    """
    parametros = util.get_parametros()
    return dominio_service.listar_dominios(parametros), 200
