from server.services import animal_service


def post_animal(body):
    return animal_service.criar_animal(body), 201
