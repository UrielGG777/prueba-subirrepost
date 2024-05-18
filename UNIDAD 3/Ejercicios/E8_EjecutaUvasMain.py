import sys
import E8_UvasMain as Interfaz
from E8_EjecutaUvasDialog import MyDialog as UvasDialog
from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow, Interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCompras.clicked.connect(self.calculaCompras)

    # Área de los Slots
    def calculaCompras(self):
        try:
            self.dialog = UvasDialog(self)
            self.dialog.setModal(True)
            self.dialog.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

