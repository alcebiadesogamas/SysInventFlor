from view.viewConfiguracao import *
from PyQt5 import QtCore, QtWidgets
from model.Amostra import Amostra
from model.Tabela import Tabela
from stateviewconfiguracao.EstadoSimulacaoViewConfiguracao import EstadoSimulacaoViewConfiguracao
from stateviewconfiguracao.EstadoSemSimulacaoViewConfiguracao import EstadoSemSimulacaoViewConfiguracao


class ControllerViewConfiguracao(QtWidgets.QMainWindow, Ui_ViewConfiguracao):
    def __init__(self, state, parent=None):
        super().__init__(parent)
        super().setupUi(self, state=state)
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
        self.btnCalcular.clicked.connect(self.operaAmostra)

    def campoAmostra(self):
        if isinstance(self.state, EstadoSemSimulacaoFormPrincipal):
            self.tfAmostras.setEnabled(False)
            self.label_7.setEnabled(False)
            # self.label_7.setText('Quantidade de Simulações:')

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

    def operaAmostra(self, diretorio: str = '', tipo: str = ''):
        tabela = Tabela(diretorio='resources/tabelat.xlsx')
        try:
            areaTotal = float(self.tfAreaTotalPopulacao.text().replace(',', '.'))
            areaParcela = float(self.tfAreaParcela.text().replace(',', '.'))
            print(int(areaTotal / areaParcela))

            tabela.setValoresTtabelado(self.cbSignificancia.currentText().strip('%'), int(areaTotal / areaParcela))
        except ValueError:
            ...
        print(self.state)
        print(tabela.valoresTtabelado)
        amostra = Amostra(tipo)
