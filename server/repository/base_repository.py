from flask import g
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import UnprocessableEntity

from server import db
from server.services import util


def gravar_objeto(objeto, commit=True):
    try:

        if hasattr(objeto, "created_by"):
            if objeto.created_by is None:
                objeto.created_by = g.username or ""

        db.session.add(objeto)

        if commit:
            db.session.commit()

        return objeto
    except IntegrityError as error:
        db.session.rollback()
        print(f'erro ao gravar {objeto.__class__.__name__}: {error.args[0]}')
        raise Exception(error.args[0])
    except Exception as error:
        db.session.rollback()
        print(f'erro ao gravar {objeto.__class__.__name__}: {error.args[0]}')
        raise Exception(error.args[0])


def atualizar_objeto(clazz, id_objeto, objeto_dto, objeto_db=None):
    if objeto_db is None:
        objeto_db = get_objeto_por_id(clazz, id_objeto)

    if objeto_db is not None:
        objeto = util.converter_dto_para_objeto(clazz, objeto_dto, objeto_db)

        if objeto is not None:
            gravar_objeto(objeto)

            return objeto

    return None


def get_objeto_por_id(clazz, id_objeto):
    try:
        query = db.session.query(clazz).filter(clazz.id == id_objeto)

        return query.first()

    except AttributeError as ex:
        print(f"Erro ao acessar atributo no get_objeto_por_id, ex: {ex}")
        db.session.rollback()
        raise UnprocessableEntity(f"Erro ao tentar acessar um atributo do objeto {clazz}, utilize o GUID ou o ID")
    except Exception as ex:
        print(f"Erro ao recuperar a boleta: {ex}")
        db.session.rollback()


def get_objetos_por_campo(clazz, campo, id_objeto):
    try:
        query = db.session.query(clazz).filter(campo == id_objeto)

        return query.all()

    except AttributeError as ex:
        print(f"Erro ao acessar atributo no get_objeto_por_id, ex: {ex}")
        db.session.rollback()
        raise UnprocessableEntity(f"Erro ao tentar acessar um atributo do objeto {clazz}, utilize o GUID ou o ID")
    except Exception as ex:
        print(f"Erro ao recuperar a boleta: {ex}")
        db.session.rollback()
