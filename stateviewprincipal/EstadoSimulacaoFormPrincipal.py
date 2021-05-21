from stateviewprincipal.EstadoSemSimulacaoFormPrincipal import *
from stateviewprincipal.StateFormPrincipal import *


class EstadoSimulacaoFormPrincipal(StateFormPrincipal):

    def __init__(self):
        super().__init__()

    def estadoSimulacao(self):
        pass

    def estadoSemSimulacao(self):
        self.estado = EstadoSemSimulacaoFormPrincipal()
