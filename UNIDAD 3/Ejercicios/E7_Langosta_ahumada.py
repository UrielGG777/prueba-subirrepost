import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E7_Langosta_ahumada.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_presupuesto)

    def calcular_presupuesto(self):
        num_personas = int(self.line_numero_personas.text())

        if num_personas <= 0:
            raise ValueError("El número de personas debe ser positivo.")

        if num_personas <= 200:
            costo_por_persona = 95.00
        elif 200 < num_personas <= 300:
            costo_por_persona = 85.00
        else:
            costo_por_persona = 75.00

        presupuesto = num_personas * costo_por_persona
        self.lb_resultado.setText(f"${presupuesto:.2f}")
        self.label_costo_persona.setText(f"${costo_por_persona:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
