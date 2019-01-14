""" Repositorio Candidatura """

from models import Candidatura


class CandidaturaRepository:
    """ Repositorio para o model Candidatura """

    @staticmethod
    def get_all_by_id_vaga(id_vaga):
        """ Busca todas as candidaturas para uma determinada vaga """
        return Candidatura.query.filter_by(
            id_vaga=id_vaga
        ).all()

    @staticmethod
    def create(id_vaga, id_pessoa, score):
        """ Cria uma nova candidatura """
        candidatura = Candidatura(
            id_vaga=id_vaga,
            id_pessoa=id_pessoa,
            score=score
        )
        return candidatura.save()
