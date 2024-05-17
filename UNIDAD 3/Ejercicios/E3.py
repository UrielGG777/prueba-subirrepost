import sys
from PyQt5 import uic, QtWidgets, QtCore

##########################################################################


qtCreatorFile1 = "E3_first_envio.ui"  # Nombre del archivo aquí.
Ui_DialogOne, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

qtCreatorFile3 = "E3_Second_EnvioInfo.ui"  # Nombre del archivo aquí.
Ui_Dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

##########################################################################


class MyDialogone(QtWidgets.QDialog, Ui_DialogOne):
    def __init__(self):
        super(MyDialogone, self).__init__()
        self.setupUi(self)

        # Área de los Signals / Configuración
        self.btn_Calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        try:
            meses = int(self.txt_meses.text())

            total = 0
            for mes in range(1, meses + 1):
                pagos = 10 * 2 ** (mes - 1)
                total += pagos


            self.dialogo = MyDialog()
            self.dialogo.setModal(False)
            self.dialogo.txt_pagos.setText(str(pagos))
            self.dialogo.txt_total.setText(str(total))
            self.dialogo.show()

        except Exception as e:
            print(e)

class MyDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(MyDialog, self).__init__()
        self.setupUi(self)

##########################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialogone()
    window.show()
    sys.exit(app.exec_())
