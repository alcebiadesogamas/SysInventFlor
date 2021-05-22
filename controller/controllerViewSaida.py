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
        string = '        ESTATÍSTICAS DA AMOSTRAGEM CASUAL SIMPLES           ' + '-'*63 + ' PARÂMETRO ESTIMADO                 '+ 'ESTIMATIVA DO PARÂMETRO' + '-'*63 
        self.teSaida.setText(string + str(self.estatistica.media))
        
    