from server import db
from server.models.usuario import Usuario


def verifica_existencia_usuario(nm_usuario):
    return db.session.query(Usuario). \
        filter(Usuario.nm_usuario == nm_usuario).first()


def verifica_existencia_cnpj(cnpj):
    return db.session.query(Usuario). \
        filter(Usuario.cnpj == cnpj).first()
