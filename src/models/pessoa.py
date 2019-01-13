"""
Definicao do model Pessoa
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Pessoa(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'pessoas'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(300), nullable=False)
    profissao = db.Column(db.String(300), nullable=False)
    localizacao = db.Column(db.String(300), nullable=False)
    nivel = db.Column(db.Integer, nullable=False)

    def __init__(self, nome, profissao, localizacao, nivel):
        """ Cria uma nova Pessoa """
        self.nome = nome
        self.profissao = profissao
        self.localizacao = localizacao
        self.nivel = nivel
