from models import Pessoa, Vaga
from repositories import CandidaturaRepository, VagaRepository, PessoaRepository


class CandidaturaService:

    def __init__(self):
        self.INF = 1E+9
        self.mapa_localidades = {
            "A": {"B": 5},
            "B": {"A": 5, "C": 7, "D": 3},
            "C": {"B": 7, "E": 4},
            "D": {"B": 3, "E": 10, "F": 8},
            "E": {"C": 4, "D": 10},
            "F": {"D": 8},
        }

    def _calcula_distancia(self, local_vaga, local_pessoa):
        """
        Determina a distancia entre a vaga e o candidato no mapa pelo algoritmo de Dijkstra
        """
        Q, dist = set(), {}
        graph = self.mapa_localidades

        if local_vaga not in graph:
            raise ValueError("O local da vaga não existe no mapa")

        if local_pessoa not in graph:
            raise ValueError("O local da pessoa não existe no mapa")

        for v in graph.keys():
            dist[v] = self.INF
            Q.add(v)
        dist[local_vaga] = 0

        while len(Q) > 0:
            u = min(Q, key=lambda v: dist[v])
            Q.remove(u)

            neighbors = set(graph[u].keys()).intersection(Q)
            for v in neighbors:
                alt = dist[u] + graph[u][v]
                if alt < dist[v]:
                    dist[v] = alt

        return dist[local_pessoa]

    def _calcula_score(self, vaga, pessoa):

        dif_nivel = vaga.nivel - pessoa.nivel
        if dif_nivel < 0:
            dif_nivel = -dif_nivel
        N = 100 - 25 * dif_nivel

        distancia = self._calcula_distancia(vaga.localizacao, pessoa.localizacao)
        if 0 <= distancia <= 5:
            D = 100
        elif 5 < distancia <= 10:
            D = 75
        elif 10 < distancia <= 15:
            D = 50
        elif 15 < distancia <= 20:
            D = 25
        else:
            D = 0

        score = (N + D) // 2

        return score

    def cria_candidatura(self, id_vaga, id_pessoa):
        vaga = VagaRepository.get_by_id(id_vaga)
        if vaga is None:
            raise ValueError("Vaga não encontrada para o id informado")

        pessoa = PessoaRepository.get_by_id(id_pessoa)
        if pessoa is None:
            raise ValueError("Pessoa não encontrada para o id informado")

        score = self._calcula_score(vaga, pessoa)

        candidatura = CandidaturaRepository.create(
            id_vaga=id_vaga,
            id_pessoa=id_pessoa,
            score=score
        )

        return candidatura
