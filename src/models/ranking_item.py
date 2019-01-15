"""
Definicao do model RankingItem
"""

class RankingItem:

    def __init__(self, nome, profissao, localizacao, nivel, score):
        """ Instancia um novo Item do Ranking """
        self.nome = nome
        self.profissao = profissao
        self.localizacao = localizacao
        self.nivel = nivel
        self.score = score
