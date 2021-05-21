from PyQt5.QtWidgets import QDialog
from view.viewDialogo import *


class ControllerViewDialogo(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.btnOkPressed)

    def btnOkPressed(self):
        self.close()
        exit(0)
