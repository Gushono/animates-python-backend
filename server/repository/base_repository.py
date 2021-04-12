from flask import g
from sqlalchemy.exc import IntegrityError

from server import db


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



