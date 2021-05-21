from model.Populacao import Populacao
from strategyamostra.EstrategiaAmostragem import EstrategiaAmostragem
from strategyestatistica.EstrategiaEstatistica import EstrategiaEstatistica


class Amostra:

    def __init__(self, tipo) -> None:
        self._populacao: Populacao
        self._amostras: list
        self._tipo = tipo
        self._estrategiaAmostragem: EstrategiaAmostragem
        self._estrategiaEstatistica: EstrategiaEstatistica

    def getAmostras(self) -> list:
        self._amostras = self._estrategiaAmostragem.colheAmostras(self._populacao)
        return self._amostras

    @property
    def populacao(self) -> Populacao:
        return self._populacao

    @populacao.setter
    def populacao(self, value: Populacao) -> None:
        self._populacao = value

    @property
    def amostras(self) -> list:
        return self._amostras

    @amostras.setter
    def amostras(self, value: list) -> None:
        self._amostras = value

    @property
    def estrategiaAmostragem(self) -> EstrategiaAmostragem:
        return self._estrategiaAmostragem

    @estrategiaAmostragem.setter
    def estrategiaAmostragem(self, value: EstrategiaAmostragem) -> None:
        self._estrategiaAmostragem = value

    @property
    def estrategiaEstatistica(self) -> EstrategiaEstatistica:
        return self._estrategiaEstatistica

    @estrategiaEstatistica.setter
    def estrategiaEstatistica(self, value: EstrategiaEstatistica) -> None:
        self._estrategiaEstatistica = value
