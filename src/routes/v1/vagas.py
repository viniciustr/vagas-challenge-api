"""
Define o blueprint para vagas
"""
from flask import Blueprint
from flask_restful import Api

from resources import UserResource
# TODO: create all resources

VAGAS_BLUEPRINT = Blueprint('vagas', __name__)


Api(VAGAS_BLUEPRINT).add_resource(
    UserResource,
    '/vagas'
)
