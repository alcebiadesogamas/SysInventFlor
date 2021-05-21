from controller.ControllerViewOpcao import *
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cfe = ControllerViewOpcao()
    cfe.show()
    qt.exec_()
