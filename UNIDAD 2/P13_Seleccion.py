import sys
from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P13_Seleccion.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.rb_badillo.clicked.connect(self.clic_badillo)
        self.rb_badillo.toggled.connect(self.toggle_badillo)
        self.rb_sofia.clicked.connect(self.clic_sofia)
        self.rb_sofia.toggled.connect(self.toggle_sofia)
        self.rb_eduardo.clicked.connect(self.clic_eduardo)
        self.rb_eduardo.toggled.connect(self.toggle_eduardo)
        self.rb_uriel.clicked.connect(self.clic_uriel)
        self.rb_uriel.toggled.connect(self.toggle_uriel)

    def clic_badillo(self):
        print("Hiciste clic a badillo xd")

    def toggle_badillo(self):
        estado = self.rb_badillo.isChecked()
        print(f"Badillocambio de estado (toggle). Nuevo Estado: {estado}")
    def clic_sofia(self):
        print("Hiciste clic a sofia xd")

    def toggle_sofia(self):
        estado = self.rb_sofia.isChecked()
        print(f"Sofia cambio de estado (toggle). Nuevo Estado: {estado}")

    def clic_eduardo(self):
           print("Hiciste clic a eduardo xd")

    def toggle_eduardo(self):
         estado = self.rb_eduardo.isChecked()
         print(f"Eduardo cambio de estado (toggle). Nuevo Estado: {estado}")
    def clic_uriel(self):
           print("Hiciste clic a uriel xd")

    def toggle_uriel(self):
         estado = self.rb_uriel.isChecked()
         print(f"Uriel cambio de estado (toggle). Nuevo Estado: {estado}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())