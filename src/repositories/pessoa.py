""" Repositorio Pessoa """

from models import Pessoa


class PessoaRepository:
    """ Repositorio para o model Pessoa """

    @staticmethod
    def get_by_id(id):
        """ Busca uma pessoa pelo seu id unico """
        return Pessoa.query.filter_by(
            id=id
        ).one()

    @staticmethod
    def create(nome, profissao, localizacao, nivel):
        """ Cria uma nova pessoa """
        pessoa = Pessoa(
            nome=nome,
            profissao=profissao,
            localizacao=localizacao,
            nivel=nivel
        )

        return pessoa.save()
