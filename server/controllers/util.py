import connexion


def get_parametros():
    parametros = {}

    for key in connexion.request.args:
        parametros[key] = connexion.request.args[key]

    return parametros
