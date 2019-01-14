"""
Define o blueprint para candidaturas
"""
from flask import Blueprint
from flask_restful import Api

from resources import CandidaturaResource


CANDIDATURAS_BLUEPRINT = Blueprint('candidaturas', __name__)
Api(CANDIDATURAS_BLUEPRINT).add_resource(
    CandidaturaResource,
    '/candidaturas'
)
