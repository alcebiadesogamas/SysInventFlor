from controller.controllerViewDialogo import ControllerViewDialogo
import controller.controllerViewOpcao as cvo
import view.viewSaida as vs
from PyQt5 import QtCore, QtWidgets
import controller.controllerViewConfiguracao as cvc
import model.Estatistica as estats

class ControllerViewSaida(QtWidgets.QMainWindow, vs.Ui_viewSaida):
    def __init__(self, estatistica: estats.Estatistica, parametros=list(), parent=None, state=None, diretorioAmostra='', tipo='') -> None:
        super().__init__(parent=parent)
        super().setupUi(self)
        self.state = state
        self.diretorioAmostra = diretorioAmostra
        self.tipo = tipo
        self.parametros = parametros
        self.estatistica = estatistica
        if(self.tipo == 'ACS'):
            self.imprimirResultadoACS()
        elif self.tipo == 'ACE':
            self.imprimirResultadoACE(result=parametros[4], eaa=parametros[6], ns=parametros[0], area_parcela=parametros[1], nparc=parametros[2], N=parametros[8], est_min_conf_erro=parametros[7], gl=parametros[5], tabela=parametros[3], ttab=parametros[9])
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
        self.btnMenuPrincipal.clicked.connect(self.mainMenu)

    def mainMenu(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = cvo.ControllerViewOpcao()
        self.ui.show()
        self.close()

    def sair(self):
        self.window = QtWidgets.QDialog()
        self.ui = ControllerViewDialogo()
        self.ui.show()

    def voltar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = cvc.ControllerViewConfiguracao(self.state, self.diretorioAmostra, self.tipo)
        self.ui.show()
        self.close()

    def imprimirResultadoACS(self):
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
      string += (f'\nO valor de ttab. bicaldal ({self.estatistica.tamAmostra - 1}; {self.estatistica.nivelSignificancia}%) = {self.estatistica.ttab[0]:.2f}\n')
      string += ('-'*122)
      string += ('\n' + ' '*30 + 'INTERVALOS DE CONFIANÇA PARA A MÉDIA E POR HECTARE\n')
      string += ('-'*122)
      string += ('\nPARA A MÉDIA\n')
      string += (f'P[{float(self.estatistica.media) - float(self.estatistica.erroDeAmostragemAbsoluto):>7.4f} ≤ µ ≤ {float(self.estatistica.media) + float(self.estatistica.erroDeAmostragemAbsoluto):>7.4f}] = {100 - float(self.estatistica.nivelSignificancia)}%')
      string += ('\nPOR HECTARE\n')
      string += (f'P[{(float(self.estatistica.media) - float(self.estatistica.erroDeAmostragemAbsoluto))*(10000/self.estatistica.areaParcela):>7.2f} ≤ µ ≤ {(float(self.estatistica.media) + float(self.estatistica.erroDeAmostragemAbsoluto))*(10000/self.estatistica.areaParcela):>7.2f}] = {100 - float(self.estatistica.nivelSignificancia)}%\n')
      string += ('-'*122)
      string += ('\n'+ ' '*30 +'TOTAL DA POPULAÇÃO\n')
      string += ('-'*122)
      string += (f'\nO total geral da população é: {self.estatistica.media*self.estatistica.AreaTotal:.2f}\n')
      string += ('-'*122)
      string += ('\n'+ ' '*30 +'INTERVALO DE CONFIANÇA PARA O TOTAL\n')
      string += (f'P[{(float(self.estatistica.media)*float(self.estatistica.AreaTotal) - float(self.estatistica.erroDeAmostragemAbsoluto)*float(self.estatistica.AreaTotal)):>7.2f} ≤ µ ≤ {(float(self.estatistica.media)*float(self.estatistica.AreaTotal) + float(self.estatistica.erroDeAmostragemAbsoluto)*float(self.estatistica.AreaTotal)):>7.2f}] = {100 - float(self.estatistica.nivelSignificancia)}%\n')
      string += ('-'*122)
      string += ('ESTIMATIVA MÍNIMA DE CONFIANÇA PARA A MÉDIA, POR HECTARE E PARA O TOTAL\n')
      string += ('-'*122)
      est_min_conf_erro_abs = float(self.estatistica.erroPadraoDaMedia)*float(self.estatistica.ttab[1])
      string += ('PARA A MÉDIA\t\t')
      string += (f'P[{float(self.estatistica.media) - est_min_conf_erro_abs:>7.4f} ≤ µ] = {100 - float(self.estatistica.nivelSignificancia)}%\n')
      string += ('POR HECTARE\t\t')
      string += (f'P[{(float(self.estatistica.media) - est_min_conf_erro_abs)*(10000/float(self.estatistica.areaParcela)):>7.2f} ≤ µ] = {100 - float(self.estatistica.nivelSignificancia)}%\n')
      string += ('PARA O TOTAL\t\t')
      string += (f'P[{(float(self.estatistica.media)* self.estatistica.AreaTotal - est_min_conf_erro_abs*self.estatistica.AreaTotal):>7.2f} ≤ µ] = {100 - float(self.estatistica.nivelSignificancia)}%\n')
      string += ('-'*122)
      string += (f'\nO valor de ttab. unicaldal ({self.estatistica.tamAmostra - 1 }; {100 - float(self.estatistica.nivelSignificancia)}%) = {float(self.estatistica.ttab[1]):.2f}')
      self.teSaida.setText(string)

    def imprimirResultadoACE(self, result, eaa, ns, area_parcela, nparc, tabela, N, est_min_conf_erro, gl, ttab):
        string = ('-' * 63 + '\n')
        string += ('       INTERVALOS DE CONFIANÇA PARA A MÉDIA E POR HECTARE\n')
        string += ('-' * 63 + '\n')
        string += ('PARA A MÉDIA        \n')
        string += (f'P[{result[4] - eaa:>7.4f} ≤ µ ≤ {result[4] + eaa:>7.4f}] = {100 - ns}%\n')
        string += ('POR HECTARE        \n')
        string += (
            f'P[{(result[4] - eaa) * (10000 / area_parcela):>7.2f} ≤ µ ≤ {(result[4] + eaa) * (10000 / area_parcela):>7.2f}] = {100 - ns}%\n')
        string += ('\n')
        string += ('-' * 63 + '\n')
        string += ('                       TOTAL DA POPULAÇÃO  \n')
        string += ('-' * 63 + '\n')
        for i in range(0, len(nparc)):
            string += (f'O total do estrato {i + 1} é: {tabela[i][2] * tabela[i][4]:.2f}\n')
        string += (f'O total geral da população é: {result[4] * N:.2f}\n')
        string += ('-' * 63 + '\n')
        string += ('\n')
        string += ('-' * 63 + '\n')
        string += ('              INTERVALO DE CONFIANÇA PARA O TOTAL       \n')
        string += ('-' * 63 + '\n')
        string += (f'P[{(result[4] * N - eaa * N):>7.2f} ≤ µ ≤ {(result[4] * N + eaa * N):>7.2f}] = {100 - ns}%\n')
        string += ('-' * 75 + '\n')
        string += ('\n')
        string += ('  ESTIMATIVA MÍNIMA DE CONFIANÇA PARA A MÉDIA, POR HECTARE E PARA O TOTAL\n')
        string += ('-' * 75 + '\n')
        string += ('PARA A MÉDIA       \n')
        string += (f'P[{result[4] - est_min_conf_erro:>7.4f} ≤ µ] = {100 - ns}%\n')
        string += ('POR HECTARE        \n')
        string += (f'P[{(result[4] - est_min_conf_erro) * (10000 / area_parcela):>7.2f} ≤ µ] = {100 - ns}%\n')
        string += ('PARA O TOTAL       \n')
        string += (f'P[{(result[4] * N - est_min_conf_erro * N):>7.2f} ≤ µ] = {100 - ns}%\n')
        string += ('-' * 75 + '\n')
        string += (f'O valor de ttab. unicaldal ({gl}; {100 - ns}%) = {ttab[3]:.2f}\n')
        self.teSaida.setText(string)
