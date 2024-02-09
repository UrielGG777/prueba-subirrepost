import math
import sys

import numpy
from PyQt5 import uic, QtWidgets
from numpy import double

qtCreatorFile = "P_10_Calificacion.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        calificaion = float(self.txtCalif.text())
        if calificaion == 10:
            nota = 'A'
        elif calificaion >= 9:
            nota = 'B'
        elif calificaion >= 8:
            nota = 'C'
        elif calificaion >= 7:
            nota = 'D'
        elif calificaion >= 6:
            nota = 'E'
        else:
            nota = 'F'
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(nota)
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

