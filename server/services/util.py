from collections import OrderedDict

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


def serialize_entidade(entidade, entidade_schema, apply_jsonify=True):
    """
   Função responsável por serializar uma ou várias entidades
   :param apply_jsonify: Responsável por applicar a função jsonify ao retorno/output
   :param entidade: List ou Entidade - Uma lista ou uma entidade, por exemplo, Cidade
   :param entidade_schema: Schema o esquema da entidade que será serialized
   :return: retorna a entidade serialized
   """
    schema = (
        entidade_schema(many=True)
        if type(entidade) == list or type(entidade) == sqlalchemy.orm.collections.InstrumentedList
        else entidade_schema()
    )
    output = (
        jsonify(schema.dump(entidade).data)
        if apply_jsonify
        else schema.dump(entidade).data
    )

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
        entidade, entidade_schema, apply_jsonify=False
    )
    pagination_serialized = serialize_entidade(
        pagination, PaginationSchema, apply_jsonify=False
    )
    pagination_serialized["items"] = entidade_serialized

    output = jsonify(pagination_serialized)

    return output


def fabrica_filtros(filtros_dict, parametros=None):
    """
    Função responsável por selecionar qual método de busca deverá ser realizado
    dependendo do filtro parâmetro passado na URL

    :param parametros: Poderá ser passado como parâmetro caso os filtros precisem ser fabricados manualmente
    :param filtros_dict: terá um dicionário com várias tuplas contendo um objeto
    de filtro e uma lista de objetos de joins, (Entidade.attr == filtro, [Entidade.entidade1, Entidade1.entidade2])

    :return: list: retorna um lista contendo dicts que representam cidades
    """
    print(f"Início criação de filtros")

    # TODO desacoplar o connexion.request.args
    parametros = parametros if parametros is not None else connexion.request.args

    pagina = int(parametros['pagina']) if 'pagina' in parametros else 1
    parametros.pop('pagina', None)

    filtros = []
    # Este set é criado para eliminar joins duplicados
    set_of_joins = OrderedDict()
    for k in parametros:
        # A variável filtro receberá o valor da função que tem o mesmo nome do parâmetro
        # recebido via query string
        filtro = (
            filtros_dict.get(k)(parametros[k])
            if filtros_dict.get(k) is not None
            else None
        )

        if filtro is None:
            # Se o filtro for vazio, significa que um parametro diferente dos registrados no servico
            # foi passado na requisicao
            continue

        if type(filtro) != tuple or len(filtro) < 2:
            raise AttributeError(
                f"O filtro {k} precisa ser uma tupla com dois valores, uma condição/filtro sql e uma lista de joins"
            )
        # Os filtros serão armazenados na lista de [filtros]
        filtros.append(filtro[0])
        if filtro[1] is not None:
            # Como cada filtro pode fazer mais de um join,
            # vamos fazer outro loop para descobrir os joins
            for i in range(len(filtro[1])):
                set_of_joins[filtro[1][i]] = None
    joins = list(set_of_joins)

    return tuple(filtros), tuple(joins), pagina


def valida_no_content_ou_no_found(filtros, lista_de_entidades):
    """
    Função responsável por validar se uma query é do tipo 404 ou 204.
    :param filtros: filtros fabricados na função fabrica_filtros
    :param lista_de_entidades: lista de entidades retornadas pela query
    """
    # Se não tem nenhum filtro e também não tem nenhuma entidade, quer dizer que não há registros no
    # banco de dados
    if len(lista_de_entidades) == 0 and len(filtros) == 0:
        print("Sem registros no banco de dados para esta consulta")
        return False
    # Se tem algum filtro e nenhuma entidade, quer dizer que a query não encontrou nenhum registro no
    # banco de dados
    elif len(lista_de_entidades) == 0 and len(filtros) > 0:
        print("Consulta não encontrou nenhum registro no banco de dados")
        return False

    return True


def valida_cnpj(cnpj):
    if cpfcnpj.validate(cnpj):
        return cnpj

    raise UnprocessableEntity(f"Erro ao validar o cnpj, verifique se o número {cnpj} é válido")
