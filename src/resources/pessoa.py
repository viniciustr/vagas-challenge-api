"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import PessoaRepository
from util import parse_params


class PessoaResource(Resource):
    """ Verbos relacionados a pessoas """

    @staticmethod
    @parse_params(
        Argument(
            'nome',
            location='json',
            required=True,
            type=str,
            help='O nome completo da pessoa deve ser informado.'
        ),
        Argument(
            'profissao',
            location='json',
            required=True,
            type=str,
            help='A profissao da pessoa deve ser especificada.'
        ),
        Argument(
            'localizacao',
            location='json',
            required=True,
            type=str,
            choices=["A", "B", "C", "D", "E", "F"],
            help="A localizacao da pessoa deve ser uma existente no mapa."
        ),
        Argument(
            'nivel',
            location='json',
            required=True,
            type=int,
            choices=range(1,6),
            help='O nivel da pessoa deve ser um inteiro na faixa especificada.'
        ),
    )
    @swag_from('../swagger/pessoa/POST.yml')
    def post(nome, profissao, localizacao, nivel):
        """ Cria uma pessoa com base nos dados enviados """
        pessoa = PessoaRepository.create(
            nome=nome,
            profissao=profissao,
            localizacao=localizacao,
            nivel=nivel
        )
        return jsonify({"pessoa": pessoa.json})
