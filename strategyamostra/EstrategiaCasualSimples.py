from model.Populacao import Populacao
from strategyamostra.EstrategiaAmostragem import EstrategiaAmostragem


class EstrategiaCasualSimples(EstrategiaAmostragem):

    def colheAmostras(self, populacao: Populacao) -> list:
        pass
#random.sample e verificar que não são amostras iguais.
