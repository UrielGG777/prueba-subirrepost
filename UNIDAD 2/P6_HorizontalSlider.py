import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P6_HorizontalSlide.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals

        self.datos_persona = {
                1: ["Badillo", "Jugar", 20, "o+", ":/variados/badillo.png"],
                2: ["Eduardo", "?", 20, "o+", ":/variados/JuarezBeltran.png"],
                3: ["Sofia", "?", 20, "o+", ":/variados/sofi.png"],
                4: ["Uriel", "?", 20, "o+", ":/variados/GonzalezUriel.png"],
            }
        self.hs_personas.setMinimum(1)
        self.hs_personas.setMaximum(4)
        self.hs_personas.setSingleStep(1)
        self.hs_personas.setValue(1)
        self.hs_personas.valueChanged.connect(self.cambia)
    # Área de los Slots
    def cambia(self):
        dataClave = self.hs_personas.value()
        print(dataClave)
        imagen = self.datos_persona[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

