import sys
from PyQt5 import uic, QtWidgets, QtCore

##########################################################################


qtCreatorFile1 = "E4_first_envio.ui"  # Nombre del archivo aquí.
Ui_DialogOne, QtBaseClass1 = uic.loadUiType(qtCreatorFile1)

qtCreatorFile3 = "E4_Second_EnvioInfo.ui"  # Nombre del archivo aquí.
Ui_Dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

##########################################################################


class MyDialogone(QtWidgets.QDialog, Ui_DialogOne):
    def __init__(self):
        super(MyDialogone, self).__init__()
        self.setupUi(self)

        # Área de los Signals / Configuración
        self.btn_Calcularsueldo.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        try:
            numempleados = int(self.txt_numempleados.text())
            hrs = int(self.txt_hrs.text())
            pagoxhora = int(self.txt_pagoxhora.text())



            sueldosemanal = hrs * pagoxhora
            pagototal = numempleados * sueldosemanal



            self.dialogo = MyDialog()
            self.dialogo.setModal(False)
            self.dialogo.txt_sueldosemanal.setText(str(sueldosemanal))
            self.dialogo.txt_totalnomina.setText(str(pagototal))
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
