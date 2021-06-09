from server import db
from server.models.relacao_match import RelacaoMatch


def verifica_existencia_match(id_animal, id_animal_match) -> RelacaoMatch:
    return db.session.query(RelacaoMatch). \
        filter(RelacaoMatch.id_animal == id_animal). \
        filter(RelacaoMatch.id_animal_match == id_animal_match).first()
