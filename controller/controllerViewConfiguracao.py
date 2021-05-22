from view.viewConfiguracao import *
from PyQt5 import QtCore, QtWidgets
from model.Amostra import Amostra
from model.Tabela import Tabela
from stateviewconfiguracao.EstadoSimulacaoViewConfiguracao import EstadoSimulacaoViewConfiguracao
from stateviewconfiguracao.EstadoSemSimulacaoViewConfiguracao import EstadoSemSimulacaoViewConfiguracao
import controller.controllerViewMetodo as cvm

class ControllerViewConfiguracao(QtWidgets.QMainWindow, Ui_ViewConfiguracao):
    def __init__(self, state, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.state = state
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )
        self.tfAreaTotalPopulacao.setValidator(QtGui.QDoubleValidator())
        self.tfAreaParcela.setValidator(QtGui.QDoubleValidator())
        self.setSignificancia()
        self.setErroAmostragem()
        self.setTaxaIntervalo()
        self.campoAmostra()
        self.btnCalcular.clicked.connect(self.calculoSemSimular) # tratar para calculoComSimulacao
        self.btnVoltar.clicked.connect(self.btnVoltarPressed)
        self.diretorioPopulacao: str
        self.tipoAmostragem: str

    def campoAmostra(self):
        if isinstance(self.state, EstadoSemSimulacaoViewConfiguracao):
            self.tfAmostras.setEnabled(False)
            self.label_7.setEnabled(False)
            self.tfNumeroSimulacoes.setEnabled(False)
            self.lblNSimulacoes.setEnabled(False)

    def setSignificancia(self):
        self.cbSignificancia.setCurrentIndex(0)
        self.cbSignificancia.addItem("1%")
        self.cbSignificancia.addItem("5%")
        self.cbSignificancia.addItem("10%")

    def setErroAmostragem(self):
        self.spbErroDeAmostragem.setRange(0, 100)
        self.spbErroDeAmostragem.setSuffix('%')

    def setTaxaIntervalo(self):
        self.spbTaxaIntervalo.setRange(0, 100)
        self.spbTaxaIntervalo.setSuffix('%')

    def btnVoltarPressed(self):
        self.ui = cvm.ControllerViewMetodo(self.state)
        self.ui.show()
        self.close()

    def calculoSemSimular(self):
        tabela = Tabela(diretorio='resources/ACS.xlsx')
        print('diretorio:', self.diretorioPopulacao, 'tipo:', self.tipoAmostragem)
        try:
            areaTotal = float(self.tfAreaTotalPopulacao.text().replace(',', '.'))
            areaParcela = float(self.tfAreaParcela.text().replace(',', '.'))
            print(int(areaTotal / areaParcela))

            tabela.setValoresTtabelado(self.cbSignificancia.currentText().strip('%'), int(areaTotal / areaParcela))
        except ValueError:
            print('deu ruim')
        print(tabela.valoresTtabelado)
        amostra = Amostra(self.tipoAmostragem)
