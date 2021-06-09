import traceback


def token_info(token):
    try:
        token = verfica_token_eh_valido(token)

        if not token:
            return None

        return {
           'usuario': 'zezinho'
        }
    except Exception as ex:
        trace = traceback.format_exc()
        msg = f"Not expected error {ex}, {trace}"
        print(msg)
        return msg


def verfica_token_eh_valido(token):
    return True if token else False
