from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.animal import AnimalSchema
from server.models.usuario import UsuarioSchema


class UsuarioAnimal(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_usuario_animal' do banco de dados
    """

    __tablename__ = "tb_usuario_animal"

    id = Column(Integer, primary_key=True)

    id_usuario = Column(Integer, ForeignKey("tb_usuario.id"))
    usuario = relationship("Usuario", foreign_keys=[id_usuario])

    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    animal = relationship("Animal", foreign_keys=[id_animal])

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class UsuarioAnimalSchema(ma.ModelSchema):
    usuario = fields.Nested(UsuarioSchema, only=('id', 'nm_usuario'))
    animal = fields.Nested(AnimalSchema)

    class Meta:
        fields = (
            "id",
            "usuario",
            "animal"
        )
