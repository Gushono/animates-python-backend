from datetime import datetime

from marshmallow import fields
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from server import db, ma
from server.models.usuario import UsuarioSchema


class Autenticacao(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_autenticacao' do banco de dados
    """

    __tablename__ = "tb_autenticacao"

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("tb_usuario.id"))
    relacao_usuario = relationship("Usuario", foreign_keys=[id_usuario])
    token = Column(String)
    expiration_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.now)


class AutenticacaoSchema(ma.ModelSchema):
    relacao_usuario = fields.Nested(UsuarioSchema, only=('id', 'email'))

    class Meta:
        fields = (
            "relacao_usuario",
            "token",
            "expiration_date",
            "created_at"
        )
