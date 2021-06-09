from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.animal import AnimalSchema


class RelacaoMatch(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_relacao_match' do banco de dados
    """

    __tablename__ = "tb_relacao_match"

    id = Column(Integer, primary_key=True)

    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    animal = relationship("Animal", foreign_keys=[id_animal])

    id_animal_match = Column(Integer, ForeignKey("tb_animal.id"))
    animal_match = relationship("Animal", foreign_keys=[id_animal_match])

    fl_match = Column(Boolean)
    fl_match_animal_match = Column(Boolean)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class RelacaoMatchSchema(ma.ModelSchema):
    animal = fields.Nested(AnimalSchema, only=('id', 'nome'))
    animal_match = fields.Nested(AnimalSchema, only=('id', 'nome'))

    class Meta:
        fields = (
            "id",
            "animal",
            "animal_match",
            "fl_match",
            "fl_match_animal_match"
        )
