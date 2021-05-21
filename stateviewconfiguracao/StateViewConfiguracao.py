from abc import ABC, abstractmethod


class StateViewConfiguracao(ABC):

    def __init__(self):
        self._estado: StateViewConfiguracao

    @abstractmethod
    def estadoSimulacao(self):
        pass

    @abstractmethod
    def estadoSemSimulacao(self):
        pass

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value
