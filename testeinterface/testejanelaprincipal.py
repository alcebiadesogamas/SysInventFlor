import sys
from view.ViewPrincipal import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Principal(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.btnSelecionarDiretorio.clicked.connect(self.openFile)
        self.setSignificancia()
        self.setErroAmostragem()

    def openFile(self):
        file, _ = QFileDialog.getOpenFileName(
            self.centralWidget(),
            'Selecionar Arquivo',
            r''
        )
        self.tfArquivoEntrada.setText(file)

    def setSignificancia(self):
        self.cbSignificancia.setCurrentIndex(0)
        self.cbSignificancia.addItem("")
        self.cbSignificancia.addItem("1%")
        self.cbSignificancia.addItem("5%")
        self.cbSignificancia.addItem("10%")

    def setErroAmostragem(self):
        self.spbErroDeAmostragem.setRange(0, 100)
        self.spbErroDeAmostragem.setSuffix('%')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Principal()
    app.show()
    qt.exec_()
