from view.viewConfiguracao import *
from PyQt5 import QtCore, QtWidgets
from model.Amostra import Amostra
import model.Tabela as tabela
import model.Estatistica as estatistica
import model.Populacao as populacao
from stateviewconfiguracao.EstadoSemSimulacaoViewConfiguracao import EstadoSemSimulacaoViewConfiguracao
import controller.controllerViewMetodo as cvm
import pandas as pd
import strategyestatistica.EstrategiaEstatisticaSimples as estatisticaACS
import controller.controllerViewSaida as cvs

class ControllerViewConfiguracao(QtWidgets.QMainWindow, Ui_ViewConfiguracao):
    def __init__(self, state, diretorioAmostra, tipo, parent=None):
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
        self.diretorioAmostra = diretorioAmostra
        self.tipoAmostragem = tipo

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
        tb = tabela.Tabela(diretorio='C:/Users/Nubia/Documents/SysInventFlor/resources/tabelat.xlsx')
        
        try:
            areaTotal = float(self.tfAreaTotalPopulacao.text().replace(',', '.'))
            
            areaParcela = float(self.tfAreaParcela.text().replace(',', '.'))
            nivelSignificancia = self.cbSignificancia.currentText().strip('%')
            tb.setValoresTtabelado(float(nivelSignificancia), len(self.getAmostras()))
            print(nivelSignificancia, len(self.getAmostras()))
            print(tb.valoresTtabelado)

            amostra = Amostra(self.tipoAmostragem)
            amostra.amostras = self.getAmostras()
            
            estatAmostra = estatistica.Estatistica()

            pop = populacao.Populacao(areaTotal=areaTotal, areaParcelas=areaParcela)

            estACS = estatisticaACS.HandlerEstatistica(estatistica=estatAmostra,ttabelado=tb, amostra=amostra.amostras, populacao=pop, nivelSignificancia=nivelSignificancia)

            estACS.calculate()

            
            
            self.window = QtWidgets.QMainWindow()
            self.ui = cvs.ControllerViewSaida(estatAmostra, state=self.state, diretorioAmostra=self.diretorioAmostra, tipo=self.tipoAmostragem)
            self.ui.show()
            self.close()

        except ValueError:
            print('Erro ao ler amostras')
        
    def getAmostras(self):
        tbAmostra = pd.read_excel(self.diretorioAmostra)
        tbAmostra = tbAmostra['Variavel'].values.tolist()
        return tbAmostra