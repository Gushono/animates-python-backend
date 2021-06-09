import base64

from werkzeug.exceptions import UnprocessableEntity

from server.models.usuario import Usuario, UsuarioSchema
from server.repository import base_repository
from server.repository.usuario_repository import verifica_existencia_usuario
from server.services.util import converter_dto_para_objeto, serialize_entidade


def criar_usuario(usuario_dto):
    try:

        if verifica_existencia_usuario(usuario_dto["email"]) is None:

            usuario = converter_dto_para_objeto(Usuario, usuario_dto)

            if usuario is not None:
                senha = criar_password_hash(usuario_dto["senha"].encode("utf-8"))
                usuario.senha = senha
                base_repository.gravar_objeto(usuario)

            return serialize_entidade(usuario, UsuarioSchema)

        raise UnprocessableEntity("Nome de usuário já existente ou cpf já existente!")
    except KeyError as ex:
        print(f"Erro ao acessar a key {ex}, verifique o seu body")
        raise UnprocessableEntity(f"Erro ao acessar a key {ex}, verifique o seu body")


def criar_password_hash(password):
    pass_encoded_str = str(base64.b64encode(password))
    pass_string_formated = pass_encoded_str.replace(pass_encoded_str[0: 2], '').replace(pass_encoded_str[-1], '')

    return pass_string_formated
