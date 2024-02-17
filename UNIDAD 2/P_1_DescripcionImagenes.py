import sys
from PyQt5 import uic, QtWidgets,QtGui

qtCreatorFile = "P1_DescripcioImagen.ui"  # Nombre del archivo aquí.
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

        self.btn_adelante.clicked.connect(self.siguiente)
        self.btn_atras.clicked.connect(self.atras)
        self.index_control = 0
        self.btn_atras.setEnabled(False)


    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_persona[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
            self.btn_atras.setEnabled(False)
    def siguiente(self):
        if self.index_control < 4:
            self.btn_atras.setEnabled(True)
            self.index_control += 1
            datos = self.datos_persona[self.index_control]
            print(datos)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))
        if self.index_control == 4:
            self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

