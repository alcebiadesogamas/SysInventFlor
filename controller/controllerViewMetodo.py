from PyQt5.QtWidgets import QMainWindow, QStyle, QFileDialog
from view.viewMetodo import *
from controller.controllerViewConfiguracao import ControllerViewConfiguracao
import controller.controllerViewOpcao as cvo

class ControllerViewMetodo(QMainWindow, Ui_ViewMetodo):

    def __init__(self, state, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.state = state
        self.leArquivo.setReadOnly(True)
        self.btnSelecionar.clicked.connect(self.openFile)
        self.btnOK.clicked.connect(self.okButtonPressed)
        self.setGeometry(
            QStyle.alignedRect(
                QtCore.Qt.LeftToRight,
                QtCore.Qt.AlignCenter,
                self.size(),
                QtWidgets.qApp.desktop().availableGeometry()
            )
        )
        self.btnVoltar.clicked.connect(self.btnVoltarPressed)
        self.setFixedSize(self.width(), self.height())

    def openFile(self) -> None:
        file, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Selecionar Arquivo',
            r''
        )
        self.leArquivo.setText(file)

    def okButtonPressed(self):
        tipo: str = str()
        if self.rbACS.isChecked():
            tipo = 'ACS'
        elif self.rbACE.isChecked():
            tipo = 'ACE'
        elif self.rbAS.isChecked():
            tipo = 'AS'
        self.window = QtWidgets.QMainWindow()
        self.ui = ControllerViewConfiguracao(self.state)
        self.ui.diretorioAmostra = self.leArquivo.text()
        self.ui.tipoAmostragem = tipo
        self.ui.show()
        self.close()

    def btnVoltarPressed(self):
        self.ui = cvo.ControllerViewOpcao()
        self.ui.show()
        self.close()
        
