import sys
from PyQt5 import uic, QtWidgets, QtCore

##########################################################################

qtCreatorFile1 = "E1_first_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile1)

class MyDialogone(QtWidgets.QDialog, Ui_dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)


        self.btn_calcular.clicked.connect(self.calcular)

    # Área de los Slots
    def calcular(self):
        self.dialogo = MyDialog(self)
        self.dialogo.setModal(True)
        self.dialogo.show()


##############3##########################

qtCreatorFile3 = "E1_Second_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)

class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btn_Accion.clicked.connect(self.accion)

    # Área de los Slots

    def accion(self):
        try:
            horas = int(self.txt_hrs.text())
            pago = int(self.txt_pago.text())

            horastotales=  horas*6
            pago = horastotales*pago
            print(horastotales)
            print(pago)

            self.acceso.txt_horas.setText(str(horastotales))
            self.acceso.txt_salario.setText(str(pago))

            self.close()
        except Exception as e:
            print(e)



##########################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialogone()
    window.show()
    sys.exit(app.exec_())