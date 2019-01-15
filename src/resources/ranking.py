"""
Define os verbos REST para Ranking
"""

from flasgger import swag_from
from flask import abort
from flask_restful import Resource
from flask_restful.reqparse import Argument
from flask.json import jsonify

from repositories import CandidaturaRepository, VagaRepository
from util import parse_params


class RankingResource(Resource):
    """ Verbos relacionados ao ranking """

    @staticmethod
    @parse_params()
    @swag_from("../swagger/ranking/GET.yml")
    def get(id_vaga):
        """ Obtem o ranking de uma vaga """
        
        vaga = VagaRepository.get_by_id(id_vaga)
        if vaga is None:
            abort(404, "Vaga não encontrada")
        
        ranking = VagaRepository.get_ranking_by_id(id_vaga)

        return jsonify([
            {
                "nome": item.nome,
                "profissao": item.profissao,
                "localizacao": item.localizacao,
                "nivel": item.nivel,
                "score": item.score
            }
            for item in ranking
        ])
