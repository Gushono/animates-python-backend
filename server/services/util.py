import connexion
import flask
import sqlalchemy.orm.collections
from flask import jsonify
from pycpfcnpj import cpfcnpj
from werkzeug.exceptions import UnprocessableEntity

from server.models.pagination import PaginationSchema


def converter_dto_para_objeto(classe, dto, objeto_db=None):
    """

    Função responsável por converter um dto para a instancia do objeto "Classe"

    :param classe: Classe que deseja utilizar
    :param dto: Contem os dados enviados para conversão

    :return: objeto: Objeto mapeado de acordo com o dto
    """

    objeto = classe()

    for key in dto:
        if isinstance(dto[key], dict):
            if key.startswith('json_'):
                setattr(objeto, key, str(dto[key]))
        elif isinstance(dto[key], list):
            setattr(objeto, key, dto[key])
        else:
            try:
                setattr(objeto, key, dto[key])
            except Exception as e:
                print(f"Erro foi: {e}")

    if objeto_db is not None:
        objeto = objeto_db

        return objeto

    return objeto


def serialize_entidade(entidade, entidade_schema):
    """
    Função responsável por serializar uma ou várias entidades

    :param entidade: Entidade que sera serializada
    :param entidade_schema: Schema da entidade
    :return: retorna a entidade serialized
    """

    if type(entidade) == list or type(entidade) == sqlalchemy.orm.collections.InstrumentedList:
        schema = entidade_schema(many=True)
    else:
        schema = entidade_schema()

    output = jsonify(schema.dump(entidade).data)

    return output


def fabrica_filtros(filtro_forcado=None):
    filtros = {}

    if not filtro_forcado:
        args = connexion.request.args
    else:
        args = filtro_forcado

    for arg in args:
        if arg not in PaginationSchema.Meta.fields:
            filtros[arg] = args[arg]
    return filtros


def serialize_pagination(entidade_schema, pagination):
    entidade = pagination.items

    entidade_serialized = serialize_entidade(
        entidade, entidade_schema
    )

    pagination_serialized = serialize_entidade(
        pagination, PaginationSchema
    )

    pagination_serialized["items"] = entidade_serialized

    output = flask.jsonify(pagination_serialized)

    return output


def valida_cnpj(cnpj):
    if cpfcnpj.validate(cnpj):
        return cnpj

    raise UnprocessableEntity(f"Erro ao validar o cnpj, verifique se o número {cnpj} é válido")
