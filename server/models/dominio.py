from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from server import db, ma


class Dominio(db.Model):
    """
    Entidade/Classe que representa a tabela 'tb_dominio' do banco de dados
    """

    __tablename__ = "tb_dominio"

    id = Column(Integer, primary_key=True)
    tp_dominio = Column(String)
    nm_dominio = Column(String)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class DominioSchema(ma.ModelSchema):

    class Meta:
        fields = (
            "id",
            "tp_dominio",
            "nm_dominio"
        )
