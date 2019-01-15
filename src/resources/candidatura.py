"""
Define os verbos REST para Candidaturas
"""

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from services import CandidaturaService
from util import parse_params


class CandidaturaResource(Resource):
    """ Verbos relacionados a candidaturas """

    @staticmethod
    @parse_params(
        Argument(
            'id_vaga',
            location='json',
            required=True,
            type=int,
            help='O id da vaga deve ser informado.'
        ),
        Argument(
            'id_pessoa',
            location='json',
            required=True,
            type=int,
            help='O id do candidato deve ser informado.'
        )
    )
    @swag_from('../swagger/candidaturas/POST.yml')
    def post(id_vaga, id_pessoa):
        """
        Cria uma candidatura com base nos dados enviados
        O score da candidatura é calculado no momento do cadastro
        """

        try:
            service = CandidaturaService()
            candidatura = service.cria_candidatura(id_vaga, id_pessoa)

            return jsonify({
                "candidatura": {
                    "id": candidatura.id,
                    "id_vaga": candidatura.id_vaga,
                    "id_pessoa": candidatura.id_pessoa
                }
            })
        except ValueError as ex:
            abort(400, ex.message)
