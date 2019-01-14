"""
Define os verbos REST para Candidaturas
"""

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import CandidaturaRepository, VagaRepository, PessoaRepository
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

        vaga = VagaRepository.get_by_id(id_vaga)
        if vaga is None:
            abort(400, "Vaga não encontrada para o id informado")
        
        pessoa = PessoaRepository.get_by_id(id_pessoa)
        if pessoa is None:
            abort(400, "Pessoa não encontrada para o id informado")

        # TODO: implementar calculo de score com base nos objetos vaga e pessoa
        score = 55

        candidatura = CandidaturaRepository.create(
            id_vaga=id_vaga,
            id_pessoa=id_pessoa,
            score=score
        )
        return jsonify({
            "candidatura": {
                "id": candidatura.id,
                "id_vaga": candidatura.id_vaga,
                "id_pessoa": candidatura.id_pessoa
            }
        })
