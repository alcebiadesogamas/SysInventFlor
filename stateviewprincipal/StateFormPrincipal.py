from abc import ABC, abstractmethod


class StateFormPrincipal(ABC):

    def __init__(self):
        self._estado: StateFormPrincipal

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
