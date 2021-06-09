from server.services import match_service


def post_match(body):
    """
    POST -> /match

    :param body: MatchVO no SWAGGER

    :return: RelacaoMatchSchema
    """

    return match_service.cria_match(body), 201


def put_match(id_match, body):
    """
    PUT -> /match/{id_match}

    :param id_match: Id da entidade de match
    :param body: MatchVO no SWAGGER

    :return: RelacaoMatchSchema
    """
    return match_service.atualiza_match(id_match, body), 200


def get_matches():
    """
    GET -> /match

    :return: PaginationRelacaoMatch
    """
    return match_service.get_matches(), 200
