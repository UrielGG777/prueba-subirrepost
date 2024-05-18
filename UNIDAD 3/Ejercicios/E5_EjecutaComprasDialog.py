import sys
import E5_ComprasDialog as Interfaz
from PyQt5 import QtWidgets

class MyDialog(QtWidgets.QDialog, Interfaz.Ui_Dialog):
    def __init__(self, vPrincipal):
        QtWidgets.QDialog.__init__(self)
        Interfaz.Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.vPrincipal = vPrincipal
        self.btnCompras_2.clicked.connect(self.exit)
        self.muestraCompras()


    # Área de los Slots
    def muestraCompras(self):
        for i in range(1, 11):
            compraCalculada = self.calculaCompras(self.vPrincipal.listaExistencias[i-1], self.vPrincipal.listaPedidos[i-1])
            getattr(self, f'txtCompra{i}').setText(str(compraCalculada))

    def calculaCompras(self, A, B):
        if A == B:
            return A
        if B > A:
            return 2 * (B - A)
        if A > B:
            return B

    def exit(self):
        self.close()

