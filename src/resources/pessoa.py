"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

# from repositories import UserRepository
from util import parse_params


class PessoaResource(Resource):
    """ Verbos relacionados a pessoas """

    @staticmethod
    @parse_params(
        Argument(
            'nome',
            location='json',
            required=True,
            help='O nome completo da pessoa.'
        ),
        Argument(
            'profissao',
            location='json',
            required=True,
            help='A profissao da pessoa.'
        ),
        Argument(
            'localizacao',
            location='json',
            required=True,
            help='A localizacao da pessoa.'
        ),
        Argument(
            'nivel',
            location='json',
            required=True,
            help='O nivel da pessoa.'
        ),
    )
    @swag_from('../swagger/pessoa/POST.yml')
    def post(nome, profissao, localizacao, nivel):
        """ Cria uma pessoa com base nos dados enviados """
        # user = UserRepository.create(
        #     last_name=last_name,
        #     first_name=first_name,
        #     age=age
        # )
        return jsonify({'user': 'AAA'})
