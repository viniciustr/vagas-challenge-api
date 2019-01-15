""" Repositorio Vaga """

from models import db, Candidatura, Pessoa, RankingItem, Vaga


class VagaRepository:
    """ Repositorio para o model Vaga """

    @staticmethod
    def get_by_id(id):
        """ Busca uma vaga pelo seu id unico """
        return Vaga.query.filter_by(
            id=id
        ).one_or_none()

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

    @staticmethod
    def get_ranking_by_id(id_vaga):
        """ Obtem o ranking de candidaturas para uma vaga """
        res = db.session.query(
            Pessoa.nome,
            Pessoa.profissao,
            Pessoa.localizacao,
            Pessoa.nivel,
            Candidatura.score
        ).select_from(
            Pessoa
        ).join(
            Candidatura, Pessoa.id == Candidatura.id_pessoa
        ).filter(
            Candidatura.id_vaga == id_vaga
        ).order_by(
            Candidatura.score.desc()
        ).all()

        return [RankingItem(item[0], item[1], item[2], item[3], item[4]) for item in res]
