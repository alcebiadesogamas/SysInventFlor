# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewSaida.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewSaida(object):
    def setupUi(self, viewSaida):
        viewSaida.setObjectName("viewSaida")
        viewSaida.resize(800, 694)
        self.centralwidget = QtWidgets.QWidget(viewSaida)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 781, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 777, 547))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.teSaida = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.teSaida.setGeometry(QtCore.QRect(0, 0, 781, 551))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.teSaida.setFont(font)
        self.teSaida.setLocale(QtCore.QLocale(QtCore.QLocale.Portuguese, QtCore.QLocale.Brazil))
        self.teSaida.setObjectName("teSaida")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 560, 781, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSair = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSair.setObjectName("btnSair")
        self.horizontalLayout.addWidget(self.btnSair)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnMenuPrincipal = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnMenuPrincipal.setObjectName("btnMenuPrincipal")
        self.horizontalLayout.addWidget(self.btnMenuPrincipal)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.btnVoltar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnVoltar.setObjectName("btnVoltar")
        self.horizontalLayout.addWidget(self.btnVoltar)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        viewSaida.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(viewSaida)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        viewSaida.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(viewSaida)
        self.statusbar.setObjectName("statusbar")
        viewSaida.setStatusBar(self.statusbar)

        self.retranslateUi(viewSaida)
        QtCore.QMetaObject.connectSlotsByName(viewSaida)

    def retranslateUi(self, viewSaida):
        _translate = QtCore.QCoreApplication.translate
        viewSaida.setWindowTitle(_translate("viewSaida", "MainWindow"))
        self.btnSair.setText(_translate("viewSaida", "Sair"))
        self.btnMenuPrincipal.setText(_translate("viewSaida", "Menu Principal"))
        self.btnVoltar.setText(_translate("viewSaida", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewSaida = QtWidgets.QMainWindow()
    ui = Ui_viewSaida()
    ui.setupUi(viewSaida)
    viewSaida.show()
    sys.exit(app.exec_())