from view.viewOpcao import *
from PyQt5.QtWidgets import QMainWindow, QStyle
from PyQt5 import QtCore
from controller.ControllerViewDialogo import ControllerViewDialogo
from controller.ControllerViewMetodo import ControllerViewMetodo
# from stateviewprincipal.StateFormPrincipal import StateFormPrincipal
from stateviewconfiguracao.EstadoSemSimulacaoViewConfiguracao import EstadoSemSimulacaoViewConfiguracao
from stateviewconfiguracao.EstadoSimulacaoViewConfiguracao import EstadoSimulacaoViewConfiguracao


class ControllerViewOpcao(QMainWindow, Ui_ViewOpcao):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.btnSair.clicked.connect(self.sair)
        self.setGeometry(
            QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )
        self.btnNaoSimular.clicked.connect(self.semSimular)
        self.btnSimulacoes.clicked.connect(self.simular)
    def sair(self):
        self.window = QtWidgets.QDialog()
        self.ui = ControllerViewDialogo()
        self.ui.show()

    def semSimular(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ControllerViewMetodo(EstadoSemSimulacaoViewConfiguracao())
        self.ui.show()
        self.close()

    def simular(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = ControllerViewMetodo(EstadoSimulacaoViewConfiguracao())
        self.ui.show()
        self.close()
