"""
Define os verbos REST para Vagas
"""

from flasgger import swag_from
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import VagaRepository
from util import parse_params


class VagaResource(Resource):
    """ Verbos relacionados a vagas """

    @staticmethod
    @parse_params(
        Argument(
            'empresa',
            location='json',
            required=True,
            type=str,
            help='O nome da empresa anunciante deve ser informado.'
        ),
        Argument(
            'titulo',
            location='json',
            required=True,
            type=str,
            help='O titulo da vaga anunciada deve ser informado.'
        ),
        Argument(
            'descricao',
            location='json',
            required=True,
            type=str,
            help='A descricao da vaga anunciada deve ser especificada.'
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
            choices=range(1, 6),
            help='O nivel da pessoa deve ser um inteiro na faixa especificada.'
        ),
    )
    @swag_from("../swagger/vagas/POST.yml")
    def post(empresa, titulo, descricao, localizacao, nivel):
        """ Cria uma vaga com base nos dados enviados """
        vaga = VagaRepository.create(
            empresa=empresa,
            titulo=titulo,
            descricao=descricao,
            localizacao=localizacao,
            nivel=nivel
        )
        return jsonify({"vaga": vaga.json})
