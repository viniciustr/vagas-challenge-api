"""
Define o blueprint para pessoas
"""
from flask import Blueprint
from flask_restful import Api

from resources import PessoaResource


PESSOAS_BLUEPRINT = Blueprint('pessoas', __name__)
Api(PESSOAS_BLUEPRINT).add_resource(
    PessoaResource,
    '/pessoas'
)
