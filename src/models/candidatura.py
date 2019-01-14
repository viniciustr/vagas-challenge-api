"""
Definicao do model Candidatura
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Candidatura(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'candidaturas'

    id = db.Column(db.Integer, primary_key=True)
    id_vaga = db.Column(db.Integer, db.ForeignKey("vagas.id"), nullable=False)
    id_pessoa = db.Column(db.Integer, db.ForeignKey("pessoas.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __init__(self, id_vaga, id_pessoa, score):
        """ Instancia uma nova Candidatura """
        self.id_vaga = id_vaga
        self.id_pessoa = id_pessoa
        self.score = score
