from controller.controllerViewDialogo import ControllerViewDialogo
import controller.controllerViewOpcao as cvo
import view.viewSaida as vs
from PyQt5 import QtCore, QtWidgets
import controller.controllerViewConfiguracao as cvc
import model.Estatistica as estats


class ControllerViewSaida(QtWidgets.QMainWindow, vs.Ui_viewSaida):
    def __init__(self, estatistica: estats.Estatistica, parametros=list(), parent=None, state=None, diretorioAmostra='',
                 tipo='') -> None:
        super().__init__(parent=parent)
        super().setupUi(self)
        self.state = state
        self.diretorioAmostra = diretorioAmostra
        self.tipo = tipo
        self.parametros = parametros
        self.estatistica = estatistica
        if (self.tipo == 'ACS'):
            self.imprimirResultadoACS()
        elif self.tipo == 'ACE':
            self.imprimirResultadoACE(result=parametros[4], eaa=parametros[6], ns=parametros[0],
                                      area_parcela=parametros[1], nparc=parametros[2], N=parametros[8],
                                      est_min_conf_erro=parametros[7], gl=parametros[5], tabela=parametros[3],
                                      ttab=parametros[9])
        self.teSaida.setReadOnly(True)
        # opens the window in screen's center
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
        N = int((self.estatistica.AreaTotal * 10000) / self.estatistica.areaParcela)
        string = ' ' * 30 + 'ESTAT??STICAS DA AMOSTRAGEM CASUAL SIMPLES           \n' + '-' * 122 + '\n PAR??METRO ESTIMADO' + ' ' * 30 + 'ESTIMATIVA DO PAR??METRO\n' + '-' * 122 + '\n'
        string += f' M??dia: {self.estatistica.media:>10.4f}\n'
        string += f' Vari??ncia: {self.estatistica.variancia:>10.4f}\n'
        string += f' Desvio Padr??o: {self.estatistica.desvioPadrao:>10.4f}\n'
        string += f' Coeficiente de varia????o: {self.estatistica.coeficienteDeVariacao:>10.4f}\n'
        string += f' Vari??ncia da m??dia: {self.estatistica.varianciaDaMedia:>10.4f}\n'
        string += f' Erro padr??o da m??dia: {self.estatistica.erroPadraoDaMedia:>10.4f}\n'
        string += f' Erro de amostragem absoluto: {self.estatistica.erroDeAmostragemAbsoluto:>10.4f}\n'
        string += f' Erro de amostragem relativo: {self.estatistica.erroDeAmostragemRelativo:>10.4f}\n'
        string += ('-' * 122)
        string += f'\nO valor de ttab. bicaldal ({self.estatistica.tamAmostra - 1}; {self.estatistica.nivelSignificancia}%) = {self.estatistica.ttab[0]:.2f}\n'
        string += ('-' * 122)
        string += ('\n' + ' ' * 30 + 'INTERVALOS DE CONFIAN??A PARA A M??DIA E POR HECTARE\n')
        string += ('-' * 122)
        string += '\nPARA A M??DIA: \t'
        string += f'P[{float(self.estatistica.media) - float(self.estatistica.erroDeAmostragemAbsoluto):>7.4f} ??? ?? ??? {float(self.estatistica.media) + float(self.estatistica.erroDeAmostragemAbsoluto):>7.4f}] = {100 - float(self.estatistica.nivelSignificancia)}%'
        string += '\nPOR HECTARE: \t'
        string += f'P[{(float(self.estatistica.media) - float(self.estatistica.erroDeAmostragemAbsoluto)) * (10000 / self.estatistica.areaParcela):>7.2f} ??? ?? ??? {(float(self.estatistica.media) + float(self.estatistica.erroDeAmostragemAbsoluto)) * (10000 / self.estatistica.areaParcela):>7.2f}] = {100 - float(self.estatistica.nivelSignificancia)}%\n'
        string += ('-' * 122)
        string += ('\n' + ' ' * 30 + 'TOTAL DA POPULA????O\n')
        string += ('-' * 122)
        string += f'\nO total geral da popula????o ??: {(self.estatistica.media * N):.2f}\n'
        string += ('-' * 122)
        string += ('\n' + ' ' * 30 + 'INTERVALO DE CONFIAN??A PARA O TOTAL\n')
        string += f'P[{(float(self.estatistica.media) * N - float(self.estatistica.erroDeAmostragemAbsoluto) * N):>7.2f} ??? ?? ??? {(float(self.estatistica.media) * N + float(self.estatistica.erroDeAmostragemAbsoluto) * N):>7.2f}] = {100 - float(self.estatistica.nivelSignificancia)}%\n '
        string += ('-' * 122)
        string += 'ESTIMATIVA M??NIMA DE CONFIAN??A PARA A M??DIA, POR HECTARE E PARA O TOTAL\n'
        string += ('-' * 122)
        est_min_conf_erro_abs = float(self.estatistica.erroPadraoDaMedia) * float(self.estatistica.ttab[1])
        string += 'PARA A M??DIA:\t'
        string += f'P[{float(self.estatistica.media) - est_min_conf_erro_abs:>7.4f} ??? ??] = {100 - float(self.estatistica.nivelSignificancia)}%\n'
        string += 'POR HECTARE:\t'
        string += f'P[{(float(self.estatistica.media) - est_min_conf_erro_abs) * (10000 / float(self.estatistica.areaParcela)):>7.2f} ??? ??] = {100 - float(self.estatistica.nivelSignificancia)}%\n'
        string += 'PARA O TOTAL:\t'
        string += f'P[{(float(self.estatistica.media) * N - est_min_conf_erro_abs * N):>7.2f} ??? ??] = {100 - float(self.estatistica.nivelSignificancia)}%\n'
        string += ('-' * 122)
        string += f'\nO valor de ttab. unicaldal ({self.estatistica.tamAmostra - 1}; {100 - float(self.estatistica.nivelSignificancia)}%) = {float(self.estatistica.ttab[1]):.2f}'
        self.teSaida.setText(string)

    def imprimirResultadoACE(self, result, eaa, ns, area_parcela, nparc, tabela, N, est_min_conf_erro, gl, ttab):
        string = ' ' * 30 + 'ESTAT??STICAS DA AMOSTRAGEM CASUAL SIMPLES           \n' + '-' * 122 + '\n PAR??METRO ESTIMADO' + ' ' * 30 + 'ESTIMATIVA DO PAR??METRO\n' + '-' * 122 + '\n'
        string += f' M??dia {result[4]:>10.4f}\n'
        string += f' Vari??ncia {result[8]:>10.4f}\n'
        string += f' Desvio Padr??o {result[7]:>10.4f}\n'
        # string += f' Coeficiente de varia????o                                                   {self.estatistica.coeficienteDeVariacao:>10.4f}\n'
        # string += f' Vari??ncia da m??dia                                                            {self.estatistica.varianciaDaMedia:>10.4f}\n'
        # string += f' Erro padr??o da m??dia                                                        {self.estatistica.erroPadraoDaMedia:>10.4f}\n'
        string += f' Erro de amostragem absoluto {eaa:>10.4f}\n'
        # string += f' Erro de amostragem relativo                                            {self.estatistica.erroDeAmostragemRelativo:>10.4f}\n'
        string += ('-' * 122 + '\n')
        string += '       INTERVALOS DE CONFIAN??A PARA A M??DIA E POR HECTARE\n'
        string += ('-' * 122 + '\n')
        string += 'PARA A M??DIA: '
        string += f'P[{result[4] - eaa:>7.4f} ??? ?? ??? {result[4] + eaa:>7.4f}] = {100 - ns}%\n'
        string += 'POR HECTARE: '
        string += (
            f'P[{(result[4] - eaa) * (10000 / area_parcela):>7.2f} ??? ?? ??? {(result[4] + eaa) * (10000 / area_parcela):>7.2f}] = {100 - ns}%\n')
        string += '\n'
        string += ('-' * 122 + '\n')
        string += '                       TOTAL DA POPULA????O  \n'
        string += ('-' * 122 + '\n')
        for i in range(0, len(nparc)):
            string += f'O total do estrato {i + 1} ??: {tabela[i][2] * tabela[i][4]:.2f}\n'
        string += f'O total geral da popula????o ??: {result[4] * N:.2f}\n'
        string += ('-' * 122 + '\n')
        string += '              INTERVALO DE CONFIAN??A PARA O TOTAL       \n'
        string += ('-' * 122 + '\n')
        string += f'P[{(result[4] * N - eaa * N):>7.2f} ??? ?? ??? {(result[4] * N + eaa * N):>7.2f}] = {100 - ns}%\n'
        string += ('-' * 122 + '\n')
        string += '\n'
        string += 'ESTIMATIVA M??NIMA DE CONFIAN??A PARA A M??DIA, POR HECTARE E PARA O TOTAL\n'
        string += ('-' * 122 + '\n')
        string += 'PARA A M??DIA: '
        string += f'P[{result[4] - est_min_conf_erro:>7.4f} ??? ??] = {100 - ns}%\n'
        string += 'POR HECTARE: '
        string += f'P[{(result[4] - est_min_conf_erro) * (10000 / area_parcela):>7.2f} ??? ??] = {100 - ns}%\n'
        string += 'PARA O TOTAL: '
        string += f'P[{(result[4] * N - est_min_conf_erro * N):>7.2f} ??? ??] = {100 - ns}%\n'
        string += ('-' * 122 + '\n')
        string += f'O valor de ttab. unicaldal ({gl}; {100 - ns}%) = {ttab[3]:.2f}\n'
        self.teSaida.setText(string)
