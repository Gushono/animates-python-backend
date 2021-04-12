from werkzeug.exceptions import UnprocessableEntity

from server.repository import conta_repository


def get_saldo_conta():
    conta = conta_repository.get_informacoes_conta()

    if conta is not None:
        return {"saldo": conta.saldo}

    raise UnprocessableEntity("Usuário possuí conta inválida!")

