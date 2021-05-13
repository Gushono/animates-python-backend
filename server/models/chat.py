from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.animal import AnimalSchema


class Chat(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_chat' do banco de dados
    """

    __tablename__ = "tb_chat"

    id = Column(Integer, primary_key=True)

    id_animal = Column(Integer, ForeignKey("tb_animal.id"))
    animal = relationship("Animal", foreign_keys=[id_animal])

    id_animal_para = Column(Integer, ForeignKey("tb_animal.id"))
    animal_para = relationship("Animal", foreign_keys=[id_animal_para])

    mensagem = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class ChatSchema(ma.ModelSchema):
    animal = fields.Nested(AnimalSchema, only=('id', 'nome'))
    animal_para = fields.Nested(AnimalSchema, only=('id', 'nome'))

    class Meta:
        fields = (
            "id",
            "animal",
            "animal_para",
            "mensagem"
        )
