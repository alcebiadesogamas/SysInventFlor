from stateviewprincipal.EstadoSimulacaoFormPrincipal import *
from stateviewprincipal.StateFormPrincipal import *


class EstadoSemSimulacaoFormPrincipal(StateFormPrincipal):

    def __init__(self):
        super().__init__()

    def estadoSimulacao(self):
        self.estado = EstadoSimulacaoFormPrincipal()

    def estadoSemSimulacao(self):
        pass
