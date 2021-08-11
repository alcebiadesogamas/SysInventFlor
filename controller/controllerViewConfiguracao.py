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
from strategyamostra.EstrategiaCasualSimples import SimulaCasualSimples
from strategyamostra.EstrategiaCasualEstratificada import EstrategiaCasualEstratificada
import strategyestatistica.EstrategiaEstatisticaEstratificada as estatisticaEstratificada
import controller.controllerViewSaida as cvs
import utils.graus_liberdade as grausDeLiberdade


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
        self.tipoAmostragem = tipo
        self.diretorioAmostra = diretorioAmostra
        self.setSignificancia()
        self.setErroAmostragem()
        self.setTaxaIntervalo()
        self.campoAmostra()
        if isinstance(self.state, EstadoSemSimulacaoViewConfiguracao):
            self.tfAmplitudeClasse.setDisabled(True)
            if self.tipoAmostragem == 'ACS':
                self.btnCalcular.clicked.connect(self.calculoSemSimularACS)
            elif self.tipoAmostragem == 'ACE':
                self.btnCalcular.clicked.connect(self.calculoSemSimularACE)
        else:
            self.btnCalcular.clicked.connect(self.calculoSimular)
            self.tfAreaTotalPopulacao.setDisabled(True)
            self.tfAreaParcela.setDisabled(True)
        self.btnVoltar.clicked.connect(self.btnVoltarPressed)
        if tipo == 'ACE':
            self.tfAreaTotalPopulacao.setDisabled(True)

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

    def calculoSemSimularACS(self):
        tb = tabela.Tabela(diretorio='./resources/tabelat.xlsx')
        
        try:
            areaTotal = float(self.tfAreaTotalPopulacao.text().replace(',', '.'))
            
            areaParcela = float(self.tfAreaParcela.text().replace(',', '.'))
            nivelSignificancia = self.cbSignificancia.currentText().strip('%')

            amostra = Amostra(self.tipoAmostragem)

            tb.setValoresTtabelado(float(nivelSignificancia), len(self.getAmostrasCasualSimples()))
            amostra.amostras = self.getAmostrasCasualSimples()
            estatAmostra = estatistica.Estatistica()
            pop = populacao.Populacao(areaTotal=areaTotal, areaParcelas=areaParcela)
            estACS = estatisticaACS.HandlerEstatistica(estatistica=estatAmostra, ttabelado=tb, amostra=amostra.amostras, populacao=pop, nivelSignificancia=nivelSignificancia)
            estACS.calculate()

            self.window = QtWidgets.QMainWindow()
            self.ui = cvs.ControllerViewSaida(estatAmostra, state=self.state, diretorioAmostra=self.diretorioAmostra, tipo=self.tipoAmostragem)
            self.ui.show()
            self.close()

        except ValueError:
            print('Erro ao ler amostras')
        
    def getAmostrasCasualSimples(self):
        tbAmostra = pd.read_excel(self.diretorioAmostra)
        tbAmostra = tbAmostra['Variavel'].values.tolist()
        return tbAmostra

    def calculoSemSimularACE(self):
        tb = tabela.Tabela(
            diretorio='./resources/tabelat.xlsx')
        amostraACE = pd.read_excel(self.diretorioAmostra,
                                   usecols=['Estratos', 'Variavel', 'Area'],
                                   dtype={'Estratos': int, 'Variavel': float, 'Area': float})
        areas = amostraACE['Area'].values.tolist()
        variavel = amostraACE['Variavel'].values.tolist()
        estratos = amostraACE['Estratos'].values.tolist()

        areaEstrato = list()
        aux = areas[0]
        areaEstrato.append(aux)
        for i in range(len(areas)):
            if areas[i] != aux:
                areaEstrato.append(areas[i])
                aux = areas[i]

        estratoAtual = estratos[0]
        nParcelasEstrato = list()
        cont = 0
        A = sum(areaEstrato)
        for indice, valor in enumerate(estratos):
            if valor == estratoAtual:
                cont += 1
            else:
                nParcelasEstrato.append(cont)
                cont = 1
                estratoAtual = valor
        nParcelasEstrato.append(cont)
        areaParcela = float(self.tfAreaParcela.text().replace(',', '.'))
        totalAreaEstrato = sum(areaEstrato)
        n = sum(nParcelasEstrato)
        N = (A*10000)/areaParcela

        handler = estatisticaEstratificada.HandlerEstatisticaEstratificada()
        result = handler.estat(variaveis=variavel, area_parcela=areaParcela, area_estrato=areaEstrato, nparc=nParcelasEstrato, N=n, A=totalAreaEstrato)

        ns = float(self.cbSignificancia.currentText().strip('%'))
        ttabelado = grausDeLiberdade.GL(tabela=result, N=n, ns=ns)

        # Configurando Parâmetros
        parametros = list()
        parametros.append(ns)
        parametros.append(areaParcela)
        parametros.append(nParcelasEstrato)
        parametros.append(result)  # tabela
        parametros.append(ttabelado[0])  # resultados
        parametros.append(ttabelado[4])  #gl
        parametros.append(ttabelado[2])  # eaa
        parametros.append(ttabelado[3])  # EstimativaMinimadeConfianca
        parametros.append(int(N))
        parametros.append(ttabelado[1])


        self.window = QtWidgets.QMainWindow()
        self.ui = cvs.ControllerViewSaida(estatistica=None, parametros=parametros, state=self.state, diretorioAmostra=self.diretorioAmostra,
                                          tipo=self.tipoAmostragem)
        self.ui.show()
        self.close()

    def calculoSimular(self):
        tamanhoAmostra = int(self.tfAmostras.text())
        nSimulacoes = int(self.tfNumeroSimulacoes.text())
        nivelSignificancia = self.cbSignificancia.currentText().strip('%')
        amp = int(self.tfAmplitudeClasse.text())
        if self.tipoAmostragem == 'ACS':
            cs = SimulaCasualSimples()
            cs.simular(tamanhoAmostra, nSimulacoes, nivelSignificancia, self.diretorioAmostra, amp)
        elif self.tipoAmostragem == 'ACE':
            ce = EstrategiaCasualEstratificada(self.diretorioAmostra, 20)
            ce.simulacoes(nSimulacoes, nivelSignificancia, amp)
