import sys
from PyQt5 import uic, QtWidgets
import numpy as np
import statistics as stat
qtCreatorFile= "Proyecto_U1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_Suma.clicked.connect(self.calcular)
        self.btn_Promedio.clicked.connect(self.calcular)
        self.btn_Mediana.clicked.connect(self.calcular)
        self.btn_Moda.clicked.connect(self.calcular)
        self.btn_desvestan.clicked.connect(self.calcular)
        self.btn_maximo.clicked.connect(self.calcular)
        self.btn_minimo.clicked.connect(self.calcular)
        self.btn_borrar.clicked.connect(self.calcular)


    # Área de los Slots
    def calcular(self):
        try:
            obj=self.sender()
            boton=obj.objectName()
            numeros = self.txt_numeros.text()
            lista = numeros.split(" ")
            lista_num=[int(i) for i in lista]
            if boton == "btn_Suma":
                operacion = sum(lista_num)
            elif boton == "btn_Promedio":
                operacion = np.average(lista_num)
            elif boton == "btn_Mediana":
                operacion = np.median(lista_num)
            elif boton == "btn_Moda":
                operacion = stat.mode(lista_num)
            elif boton == "btn_desvestan":
                operacion = stat.stdev(lista_num)
            elif boton == "btn_maximo":
                operacion = np.max(lista_num)
            elif boton == "btn_minimo":
                operacion = np.min(lista_num)
            else:
                operacion = ""
                self.txt_numeros.setText("")
            self.txt_resultado.setText(str(operacion))
        except Exception as error:
            print(error)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())