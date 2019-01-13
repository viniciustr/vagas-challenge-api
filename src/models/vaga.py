"""
Definicao do model Vaga
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Vaga(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'vagas'

    id = db.Column(db.Integer, primary_key=True)
    empresa = db.Column(db.String(300), nullable=False)
    titulo = db.Column(db.String(300), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)
    localizacao = db.Column(db.String(300), nullable=False)
    nivel = db.Column(db.Integer, nullable=False)

    def __init__(self, empresa, titulo, descricao, localizacao, nivel):
        """ Instancia uma nova Vaga """
        self.empresa = empresa
        self.titulo = titulo
        self.descricao = descricao
        self.localizacao = localizacao
        self.nivel = nivel
