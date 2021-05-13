from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.dominio import DominioSchema


class Animal(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_animal' do banco de dados
    """

    __tablename__ = "tb_animal"

    id = Column(Integer, primary_key=True)
    id_tp_animal = Column(Integer, ForeignKey("tb_dominio.id"))
    dominio_tp_animal = relationship("Dominio", foreign_keys=[id_tp_animal])

    nome = Column(String)
    descricao = Column(String)
    fl_buscando_parceiro = Column(Boolean)
    fl_para_adocao = Column(Boolean)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class AnimalSchema(ma.ModelSchema):
    dominio_tp_animal = fields.Nested(DominioSchema, only=('id', 'nm_dominio'))

    class Meta:
        fields = (
            "id",
            "dominio_tp_animal",
            "nome",
            "descricao",
            "fl_buscando_parceiro",
            "fl_para_adocao",
        )
