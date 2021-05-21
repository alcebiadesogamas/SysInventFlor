from abc import ABC, abstractmethod
from model.Populacao import Populacao


class EstrategiaAmostragem(ABC):

    @abstractmethod
    def colheAmostras(self, populacao: Populacao) -> list:
        pass
