from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.animal import AnimalSchema


class Denuncia(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_denuncia' do banco de dados
    """

    __tablename__ = "tb_denuncia"

    id = Column(Integer, primary_key=True)

    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    animal = relationship("Animal", foreign_keys=[id_animal])

    motivo = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class DenunciaSchema(ma.ModelSchema):
    animal = fields.Nested(AnimalSchema, only=('id', 'nome'))

    class Meta:
        fields = (
            "id",
            "animal",
            "motivo"
        )
