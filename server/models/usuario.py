from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from server import db, ma


class Usuario(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_usuario' do banco de dados
    """

    __tablename__ = "tb_usuario"

    id = Column(Integer, primary_key=True)
    nm_usuario = Column(String, unique=True)
    cpf = Column(String, unique=True)
    senha = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    updated_by = Column(String)


class UsuarioSchema(ma.ModelSchema):
    class Meta:
        fields = (
            "id",
            "nm_usuario",
            "cpf",
            "created_at",
        )
