import sys
import E5_ProductosMain as Interfaz
from E5_EjecutaComprasDialog import MyDialog as ComprasDialog
from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow, Interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCompras.clicked.connect(self.calculaCompras)
        self.listaExistencias = []
        self.listaPedidos = []

    # Área de los Slots
    def calculaCompras(self):
        try:
            self.listaPedidos.clear()
            self.listaExistencias.clear()
            for i in range(1, 11):
                self.listaExistencias.append(int(getattr(self, f'txtExistencia{i}').text()))
                self.listaPedidos.append(int(getattr(self, f'txtPedido{i}').text()))
            self.dialog = ComprasDialog(self)
            self.dialog.setModal(True)
            self.dialog.show()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

