from flask import jsonify
from pycpfcnpj import cpfcnpj
from werkzeug.exceptions import UnprocessableEntity
import sqlalchemy.orm.collections


def converter_dto_para_objeto(classe, dto):
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


def valida_cnpj(cnpj):
    if cpfcnpj.validate(cnpj):
        return cnpj

    raise UnprocessableEntity(f"Erro ao validar o cnpj, verifique se o número {cnpj} é válido")
