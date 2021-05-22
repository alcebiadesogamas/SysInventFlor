import controller.controllerViewOpcao as cvo
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cfe = cvo.ControllerViewOpcao()
    cfe.show()
    qt.exec_()
