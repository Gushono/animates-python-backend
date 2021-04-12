from werkzeug.exceptions import UnprocessableEntity

from server.models.transacoes import TransacaoSchema
from server.repository import transacao_repository
from server.services import util


def listar_transacoes(params):
    transacoes = transacao_repository.listar_transacoes(params)

    if transacoes:
        return util.serialize_entidade(transacoes, TransacaoSchema)

    return []


def listar_ultima_transacao():
    transacao = transacao_repository.lista_ultima_transacao()

    if transacao:
        return util.serialize_entidade(transacao, TransacaoSchema)

    raise UnprocessableEntity("Erro ao retornar a transação")
