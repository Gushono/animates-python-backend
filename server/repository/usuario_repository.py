from server import db
from server.models.usuario import Usuario


def verifica_existencia_usuario(email):
    return db.session.query(Usuario). \
        filter(Usuario.email == email).first()


