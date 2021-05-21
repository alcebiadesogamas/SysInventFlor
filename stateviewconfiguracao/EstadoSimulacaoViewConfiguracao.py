from stateviewconfiguracao.EstadoSemSimulacaoViewConfiguracao import *
from stateviewconfiguracao.StateViewConfiguracao import *


class EstadoSimulacaoViewConfiguracao(StateViewConfiguracao):

    def __init__(self):
        super().__init__()

    def estadoSimulacao(self):
        pass

    def estadoSemSimulacao(self):
        self.estado = EstadoSemSimulacaoViewConfiguracao()
