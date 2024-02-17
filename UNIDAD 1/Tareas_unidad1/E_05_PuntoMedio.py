import math
import sys
from PyQt5 import uic, QtWidgets
from numpy import double

qtCreatorFile = "E_05_PuntoMedio.ui"  # Nombre del archivo aquí.
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
        punto1 = []
        punto2 = []
        punto1.append(float(self.txtX1.text()))
        punto1.append(float(self.txtY1.text()))
        punto2.append(float(self.txtX2.text()))
        punto2.append(float(self.txtY2.text()))
        xMedia = (punto1[0] + punto2[0]) / 2
        yMedia = (punto1[1] + punto2[1]) / 2
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText("({0}, {1})".format(xMedia, yMedia))
        messageBox.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

