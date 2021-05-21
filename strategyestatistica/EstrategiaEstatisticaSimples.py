import numpy as np
from model.Estatistica import Estatistica
from model.Tabela import Tabela
from model.Populacao import Populacao


class HandlerEstatistica:

    def __init__(self, estatistica: Estatistica, ttabelado: Tabela, amostra: list, populacao: Populacao,
                 nivelSignificancia: float):
        self._estatistica: Estatistica = estatistica
        self._amostra = amostra
        self._ttabelado = ttabelado
        self._populacao = populacao
        self._nivelSignificancia = nivelSignificancia

    def calculate(self):
        self._estatistica.somatorio = np.sum(self._amostra)
        self._estatistica.somatorioQuadrado = np.sum(np.power(self._amostra, 2))
        self._estatistica.media = np.mean(self._amostra)
        self._estatistica.variancia = np.var(self._amostra)
        self._estatistica.desvioPadrao = np.std(self._amostra)

        self._estatistica.coeficienteDeVariacao = (self._estatistica.variancia / self._estatistica.media) * 100
        self._estatistica.fFracaoDeAmostragem = (len(self._amostra) / self._populacao.totalParcelas)

        if self._estatistica.fFracaoDeAmostragem <= 0.05:
            self._populacao.tipo = 'Finita'
            self._estatistica.varianciaDaMedia = (self._estatistica.variancia / len(self._amostra))
        else:
            self._populacao.tipo = 'Infinita'
            self._estatistica.varianciaDaMedia = (self._estatistica.variancia / len(self._amostra)) * (1 - self._estatistica.fFracaoDeAmostragem)
        self._estatistica.erroPadraoDaMedia = self._estatistica.varianciaDaMedia ** (1 / 2)
        self._estatistica.erroDeAmostragemAbsoluto = self._estatistica.erroPadraoDaMedia * self._ttabelado.valoresTtabelado[0]
        self._estatistica.erroDeAmostragemRelativo = (self._estatistica.erroDeAmostragemAbsoluto / self._estatistica.media) * 100
