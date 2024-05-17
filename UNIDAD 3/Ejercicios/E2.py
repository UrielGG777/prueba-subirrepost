import sys
from PyQt5 import uic, QtWidgets

##########################################################################

qtCreatorFile1 = "E2_first_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile1)


class MyDialogone(QtWidgets.QDialog, Ui_dialog):
    datos_ventas = []  # Definir datos_ventas como una variable de clase compartida

    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        self.btn_NuevaVenta.clicked.connect(self.NuevaVenta)
        self.btn_CatA.clicked.connect(self.CatA)
        self.btn_CatB.clicked.connect(self.CatB)
        self.btn_CatC.clicked.connect(self.CatC)
        self.btn_vtotal.clicked.connect(self.VentasTotales)
        self.btn_ventaxcategoria.clicked.connect(self.ventacat)
        self.btn_Salir.clicked.connect(self.salir)

    # Área de los Slots
    def NuevaVenta(self):
        self.dialogo = MyDialog(self)
        self.dialogo.setModal(True)
        self.dialogo.show()

    def CatA(self):
        try:
            ventasA = 0
            self.datos.clear()

            for venta in MyDialogone.datos_ventas:
                nombre_venta, monto_venta = venta

                if monto_venta > 1000:
                    ventasA += 1
                    self.datos.addItem("Venta: "+nombre_venta + ", Monto: " + "$ "+str(monto_venta))

            print(ventasA)

        except Exception as e:
            print(e)

    def CatB(self):
        try:
            ventasB = 0
            self.datos.clear()

            for venta in MyDialogone.datos_ventas:
                nombre_venta, monto_venta = venta

                if 500 < monto_venta <= 1000:
                    ventasB += 1
                    self.datos.addItem("Venta: "+nombre_venta + ", Monto: " + "$ "+str(monto_venta))


            print(ventasB)
        except Exception as e:
            print(e)

    def CatC(self):
        try:
            ventasC = 0
            self.datos.clear()

            for venta in MyDialogone.datos_ventas:
                nombre_venta, monto_venta = venta

                if monto_venta <= 500:
                    ventasC += 1

                    self.datos.addItem("Venta: "+nombre_venta + ", Monto: " + "$ "+str(monto_venta))

            print(ventasC)
        except Exception as e:
            print(e)

    def ventacat(self):
            try:
                # Inicializar contadores para cada categoría
                total_catA = 0
                total_catB = 0
                total_catC = 0

                # Limpiar el QListWidget antes de agregar nuevos elementos
                self.datos.clear()

                for nombre_venta, monto_venta in MyDialogone.datos_ventas:
                    if monto_venta > 1000:
                        total_catA += monto_venta
                    elif 500 < monto_venta <= 1000:
                        total_catB += monto_venta
                    elif monto_venta <= 500:
                        total_catC += monto_venta

                # Mostrar las ventas por categoría
                self.datos.addItem("Ventas categoría A: $" + str(total_catA))
                self.datos.addItem("Ventas categoría B: $" + str(total_catB))
                self.datos.addItem("Ventas categoría C: $" + str(total_catC))

            except Exception as e:
                print(e)

    def VentasTotales(self):
        try:
            total_ventas = 0
            self.datos.clear()

            for nombre_venta, monto_venta in MyDialogone.datos_ventas:
                total_ventas += monto_venta

                self.datos.addItem("Total: "+ str(total_ventas))

            print(total_ventas)

        except Exception as e:
            print(e)

    def salir(self):
        try:
            sys.exit(app.exec_())
        except Exception as e:
            print(e)

########################################

qtCreatorFile3 = "E2_Second_RecepcionInfo.ui"  # Nombre del archivo aquí.
Ui_dialog, QtBaseClass3 = uic.loadUiType(qtCreatorFile3)


class MyDialog(QtWidgets.QDialog, Ui_dialog):
    def __init__(self, rPrincipal):
        QtWidgets.QDialog.__init__(self)
        Ui_dialog.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.acceso = rPrincipal

        self.btn_AgregarVenta.clicked.connect(self.agregar)

    # Área de los Slots
    def agregar(self):
        try:
            nombreVenta = self.txt_NombreVenta.text()
            montoVenta = int(self.txt_montoVenta.text())

            MyDialogone.datos_ventas.append((nombreVenta, montoVenta))  # Agregar los datos a la lista

            print(MyDialogone.datos_ventas)



            self.close()
        except Exception as e:
            print(e)


##########################################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialogone()
    window.show()
    sys.exit(app.exec_())
