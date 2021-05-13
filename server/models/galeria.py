from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.animal import AnimalSchema


class Galeria(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_galeria' do banco de dados
    """

    __tablename__ = "tb_galeria"

    id = Column(Integer, primary_key=True)

    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    animal = relationship("Animal", foreign_keys=[id_animal])

    url_foto = Column(String)

    fl_foto_principal = Column(Boolean)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class GaleriaSchema(ma.ModelSchema):
    animal = fields.Nested(AnimalSchema, only=('id', 'nome'))

    class Meta:
        fields = (
            "id",
            "animal",
            "url_foto",
            "fl_foto_principal"
        )
