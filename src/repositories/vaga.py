""" Repositorio Vaga """

from models import Vaga


class VagaRepository:
    """ Repositorio para o model Vaga """

    @staticmethod
    def get_by_id(id):
        """ Busca uma vaga pelo seu id unico """
        return Vaga.query.filter_by(
            id=id
        ).one()

    @staticmethod
    def create(empresa, titulo, descricao, localizacao, nivel):
        """ Cria uma nova vaga """
        vaga = Vaga(
            empresa=empresa,
            titulo=titulo,
            descricao=descricao,
            localizacao=localizacao,
            nivel=nivel
        )

        return vaga.save()
