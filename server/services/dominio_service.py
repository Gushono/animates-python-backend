from server.models.dominio import Dominio, DominioSchema
from server.repository import base_repository


def listar_dominios(parametros):
    print(f"Iniciando a listagem de dominios... \n {parametros}")
    return base_repository.listar(Dominio, DominioSchema, parametros)
