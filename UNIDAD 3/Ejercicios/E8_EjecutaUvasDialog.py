import sys
import E8_UvasDialog as Interfaz
from PyQt5 import QtWidgets

class MyDialog(QtWidgets.QDialog, Interfaz.Ui_Dialog):
    def __init__(self, vPrincipal):
        QtWidgets.QDialog.__init__(self)
        Interfaz.Ui_Dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.vPrincipal = vPrincipal
        self.txtOK.clicked.connect(self.exit)
        self.muestraPrecio()


    # Área de los Slots
    def muestraPrecio(self):
        precio = int(self.vPrincipal.txtPrecio.text())
        if self.vPrincipal.rtbnTipoA.isChecked():
            if self.vPrincipal.rbtnTamano1.isChecked():
                precio += 20
            else:
                precio += 30
        else:
            if self.vPrincipal.rbtnTamano1.isChecked():
                precio -= 30
            else:
                precio -= 50
        self.txtPrecioKilo.setText(str(precio))

    def exit(self):
        self.close()

