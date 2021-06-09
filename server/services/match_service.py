import flask
from werkzeug.exceptions import NotFound

from server.models.relacao_match import RelacaoMatch, RelacaoMatchSchema
from server.repository import base_repository
from server.services import util
from server.services.util import converter_dto_para_objeto


def cria_match(match_dto):
    try:
        match = converter_dto_para_objeto(RelacaoMatch, match_dto)

        if match:
            base_repository.gravar_objeto(match)

            return util.serialize_entidade(match, RelacaoMatchSchema)

    except Exception as ex:
        print(ex)
        raise ex


def atualiza_match(id_match, match_dto):
    try:
        match = base_repository.get_objeto_por_id(RelacaoMatch, id_match)

        if match:
            match.id_animal_match = match_dto.get('id_animal_match')
            match.fl_animal_match = match_dto.get('fl_animal_match')

            base_repository.gravar_objeto(match)

            return util.serialize_entidade(match, RelacaoMatchSchema)
        raise NotFound('Entidade não encontrada')
    except NotFound as ex:
        print(ex)
        raise ex
    except Exception as ex:
        print(ex)
        raise ex


def get_matches():
    try:
        user = flask.g.usuario_autenticado.email

        filtros = util.fabrica_filtros({"solicitante": user})

        pagination_matches = RelacaoMatch.query.filter_by(**filtros).paginate(
            per_page=40,
            max_per_page=50)

        return util.serialize_pagination(RelacaoMatchSchema, pagination_matches)

    except Exception as ex:
        print(ex)
        raise ex

# def recebe_matches()
