import sys
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

qtCreatorFile = "E9_viaje_de_estudios.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcular_costos)

    def calcular_costos(self):
        num_alumnos = int(self.line_numAlumnos.text())
        if num_alumnos >= 100:
            costo_por_alumno = 65.00
            costo_total = num_alumnos * costo_por_alumno
        elif 50 <= num_alumnos < 100:
            costo_por_alumno = 70.00
            costo_total = num_alumnos * costo_por_alumno
        elif 30 <= num_alumnos < 50:
            costo_por_alumno = 95.00
            costo_total = num_alumnos * costo_por_alumno
        else:
            costo_por_alumno = 4000.00 / num_alumnos
            costo_total = 4000.00

        self.label_costo_alumno.setText(f" ${costo_por_alumno:.2f}")
        self.label_costo_total.setText(f"${costo_total:.2f}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
