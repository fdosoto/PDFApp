import sys, os, io
from img import Ui_Img
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
if hasattr(sys, 'frozen'):

    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

class Ui_MainWindow(object):

    def img (self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Img()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(553, 621)
        MainWindow.setWindowIcon(QtGui.QIcon('PDF.ico'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnExaminar = QtWidgets.QPushButton(self.centralwidget)
        self.btnExaminar.setGeometry(QtCore.QRect(460, 30, 75, 23))
        self.btnExaminar.setObjectName("btnExaminar")
        self.txtRuta = QtWidgets.QTextEdit(self.centralwidget)
        self.txtRuta.setGeometry(QtCore.QRect(10, 33, 421, 31))
        self.txtRuta.setObjectName("txtRuta")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 90, 421, 381))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.btnGuardar = QtWidgets.QPushButton(self.centralwidget)
        self.btnGuardar.setGeometry(QtCore.QRect(360, 490, 75, 23))
        self.btnGuardar.setObjectName("btnGuardar")
        self.btnImagenes = QtWidgets.QPushButton(self.centralwidget)
        self.btnImagenes.setGeometry(QtCore.QRect(460, 90, 75, 23))
        self.btnImagenes.setObjectName("btnImagenes")
        self.btnImagenes.clicked.connect(self.img)
        self.btnUnir = QtWidgets.QPushButton(self.centralwidget)
        self.btnUnir.setGeometry(QtCore.QRect(460, 150, 75, 23))
        self.btnUnir.setObjectName("btnUnir")
        self.btnRotar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRotar.setGeometry(QtCore.QRect(460, 210, 75, 23))
        self.btnRotar.setObjectName("btnRotar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 553, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExaminar.setText(_translate("MainWindow", "Examinar"))
        self.btnGuardar.setText(_translate("MainWindow", "Guardar"))
        self.btnImagenes.setText(_translate("MainWindow", "Imágenes"))
        self.btnUnir.setText(_translate("MainWindow", "Unir"))
        self.btnRotar.setText(_translate("MainWindow", "Rotar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
