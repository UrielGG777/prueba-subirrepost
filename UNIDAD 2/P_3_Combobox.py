import sys
from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = "P3_Combobox.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_persona = {
            1:["Badillo", "Jugar", 20, "o+", ":/variados/badillo.png"],
            2: ["Eduardo", "?", 20, "o+", ":/variados/JuarezBeltran.png"],
            3: ["Sofia", "?", 20, "o+", ":/variados/sofi.png"],
            4: ["Uriel", "?", 20, "o+", ":/variados/GonzalezUriel.png"],
        }

        self.combo_persona.addItem("Selecciona...", 0)
        self.combo_persona.addItem("Badillo", 1)
        self.combo_persona.addItem("Eduardo", 2)
        self.combo_persona.addItem("Sofia", 3)
        self.combo_persona.addItem("Uriel", 4)

        self.combo_persona.currentIndexChanged.connect(self.cambia)

    def cambia(self):
        print("Text " + self.combo_persona.currentText())
        print("Index " + str(self.combo_persona.currentIndex()))
        print("Data " + str(self.combo_persona.currentText))

        dataClave = self.combo_persona.currentData()
        imagen = self.datos_persona[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

