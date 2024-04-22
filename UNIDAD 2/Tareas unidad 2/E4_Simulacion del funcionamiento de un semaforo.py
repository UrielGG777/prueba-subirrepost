import sys
from PyQt5 import uic, QtWidgets,QtGui
from PyQt5.QtGui import QPixmap

qtCreatorFile = "IMC.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btnCalcular.clicked.connect(self.calcular_imc)
        self.btnLimpiar.clicked.connect(self.limpiar)

    # Área de los Slots
    def calcular_imc(self):
        try:
            peso = float(self.txtPeso.text())
            altura = float(self.txtAltura.text())
            imc = peso / altura**2
            self.txtIMC.setText(f"{imc:.2f}")


            if imc < 18.5:
                self.txtRecomendacion.setText("Tu IMC es bajo. Considera aumentar tu peso de manera saludable.");
                self.rec1.setPixmap(QtGui.QPixmap(":/IMCBajo/Imagenes/IMCbajo1.jpg"))
                self.rec2.setPixmap(QtGui.QPixmap(":/IMCBajo/Imagenes/IMCbajo2.jpg"))
                self.rec3.setPixmap(QtGui.QPixmap(":/IMCBajo/Imagenes/IMCbajo3.jpg"))
                self.rec4.setPixmap(QtGui.QPixmap(":/IMCBajo/Imagenes/IMCbajo4.jpg"))

            elif 18.5 <= imc < 25:
                self.txtRecomendacion.setText("Tu IMC está en un rango saludable. ¡Sigue así!");
                self.rec1.setPixmap(QtGui.QPixmap(":/IMCsaludable/Imagenes/IMCsaludable1.jpg"))
                self.rec2.setPixmap(QtGui.QPixmap(":/IMCsaludable/Imagenes/IMCsaludable2.jpg"))
                self.rec3.setPixmap(QtGui.QPixmap(":/IMCsaludable/Imagenes/IMCsaludable3.jpg"))
                self.rec4.setPixmap(QtGui.QPixmap(":/IMCsaludable/Imagenes/IMCsaludable4.jpg"))


            elif 25 <= imc < 30:
                self.txtRecomendacion.setText("Tienes sobrepeso. Considera adoptar hábitos de vida más saludables.");
                self.rec1.setPixmap(QtGui.QPixmap(":/IMCsobrepeso/Imagenes/IMCsobrepeso1.jpg"))
                self.rec2.setPixmap(QtGui.QPixmap(":/IMCsobrepeso/Imagenes/IMCsobrepeso2.jpg"))
                self.rec3.setPixmap(QtGui.QPixmap(":/IMCsobrepeso/Imagenes/IMCsobrepeso3.jpg"))
                self.rec4.setPixmap(QtGui.QPixmap(":/IMCsobrepeso/Imagenes/IMCsobrepeso4.jpg"))


            else:
                self.txtRecomendacion.setText("Tienes obesidad. Consulta a un profesional de la salud para recibir asesoramiento.")
                self.rec1.setPixmap(QtGui.QPixmap(":/IMCobsedidad/Imagenes/IMCobesidad1.jpg"))
                self.rec2.setPixmap(QtGui.QPixmap(":/IMCobsedidad/Imagenes/IMCobesidad2.jpg"))
                self.rec3.setPixmap(QtGui.QPixmap(":/IMCobsedidad/Imagenes/IMCobesidad3.jpg"))
                self.rec4.setPixmap(QtGui.QPixmap(":/IMCobsedidad/Imagenes/IMCobesidad4.jpg"))
                #imagen_path = "obesidad_imagen.png"
        except Exception as error:
            print(error)

    def limpiar(self):
        self.txtPeso.setText("")
        self.txtAltura.setText("")
        self.txtIMC.setText("")
        self.rec1.setPixmap(QtGui.QPixmap(""))
        self.rec2.setPixmap(QtGui.QPixmap(""))
        self.rec3.setPixmap(QtGui.QPixmap(""))
        self.rec4.setPixmap(QtGui.QPixmap(""))
        self.txtRecomendacion.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

