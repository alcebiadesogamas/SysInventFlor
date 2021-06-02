from controller.controllerViewDialogo import ControllerViewDialogo
import view.viewSaida as vs
from PyQt5 import QtCore, QtWidgets
import controller.controllerViewConfiguracao as cvc
import model.Estatistica as estats

class ControllerViewSaida(QtWidgets.QMainWindow, vs.Ui_viewSaida):
    def __init__(self, estatistica: estats.Estatistica, parent=None, state=None, diretorioAmostra='', tipo='') -> None:
        super().__init__(parent=parent)
        super().setupUi(self)
        self.state = state
        self.diretorioAmostra = diretorioAmostra
        self.tipo = tipo
        self.estatistica = estatistica
        self.imprimirResultado()
        self.teSaida.setReadOnly(True)
        #opens the window in screen's center
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )
        self.btnSair.clicked.connect(self.sair)
        self.btnVoltar.clicked.connect(self.voltar)

    def sair(self):
        self.window = QtWidgets.QDialog()
        self.ui = ControllerViewDialogo()
        self.ui.show()

    def voltar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = cvc.ControllerViewConfiguracao(self.state, self.diretorioAmostra, self.tipo)
        self.ui.show()
        self.close()
    
    def imprimirResultado(self):
        string = ' '*30 +'ESTATÍSTICAS DA AMOSTRAGEM CASUAL SIMPLES           \n'+'-'*122 + '\n PARÂMETRO ESTIMADO'+ ' '*30 +'ESTIMATIVA DO PARÂMETRO\n' + '-'*122 + '\n' 
        string += (f' Média                                                                               {self.estatistica.media:>10.4f}\n')
        string += (f' Variância                                                                          {self.estatistica.variancia:>10.4f}\n')
        string += (f' Desvio Padrão                                                                  {self.estatistica.desvioPadrao:>10.4f}\n')
        string += (f' Coeficiente de variação                                                   {self.estatistica.coeficienteDeVariacao:>10.4f}\n')
        string += (f' Variância da média                                                            {self.estatistica.varianciaDaMedia:>10.4f}\n')
        string += (f' Erro padrão da média                                                        {self.estatistica.erroPadraoDaMedia:>10.4f}\n')
        string += (f' Erro de amostragem absoluto                                           {self.estatistica.erroDeAmostragemAbsoluto:>10.4f}\n')
        string += (f' Erro de amostragem relativo                                            {self.estatistica.erroDeAmostragemRelativo:>10.4f}\n')
        string += ('-'*122)
        # string += (f'O valor de ttab. bicaldal ({n - 1}; {ns}%) = {ttab:.2f}')
        self.teSaida.setText(string )
        
    