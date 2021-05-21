from abc import ABC, abstractmethod
from model.Estatistica import *
from model.Tabela import *


class EstrategiaEstatistica(ABC):

    def __init__(self):
        self._estatistica: Estatistica
        self._tabela: Tabela

    @abstractmethod
    def calculate(self) -> None:
        pass
