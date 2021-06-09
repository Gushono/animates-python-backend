from werkzeug.exceptions import UnprocessableEntity

from server.models.animal import Animal
from server.models.usuario_animal import UsuarioAnimal, UsuarioAnimalSchema
from server.repository import base_repository
from server.services.util import converter_dto_para_objeto, serialize_entidade


def criar_animal(body):
    try:

        animal = converter_dto_para_objeto(Animal, body)

        if animal:
            base_repository.gravar_objeto(animal, commit=False)
            usuario_animal = gera_usuario_animal(body['id_usuario'], animal)

            return serialize_entidade(usuario_animal, UsuarioAnimalSchema)

        raise UnprocessableEntity("Erro em alguma chave enviada, verifique o body: ", body)
    except KeyError as ex:
        print(f"Erro ao acessar a key {ex}, verifique o seu body")
        raise UnprocessableEntity(f"Erro ao acessar a key {ex}, verifique o seu body")


def gera_usuario_animal(id_usuario, animal):

    try:
        usuario_animal = UsuarioAnimal()

        usuario_animal.animal = animal
        usuario_animal.id_usuario = id_usuario

        base_repository.gravar_objeto(usuario_animal)

        return usuario_animal
    except Exception as ex:
        print(ex)
        raise ex
