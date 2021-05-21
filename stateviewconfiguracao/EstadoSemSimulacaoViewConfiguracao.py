from stateviewconfiguracao.EstadoSimulacaoViewConfiguracao import *
from stateviewconfiguracao.StateViewConfiguracao import *


class EstadoSemSimulacaoViewConfiguracao(StateViewConfiguracao):

    def __init__(self):
        super().__init__()

    def estadoSimulacao(self):
        self.estado = EstadoSimulacaoViewConfiguracao()

    def estadoSemSimulacao(self):
        pass
