import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_Seleccion_equipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signal
        self.cb_badillo.toggled.connect(self.sel_badillo)
        self.cb_sofia.toggled.connect(self.sel_sofia)
        self.cb_eduardo.toggled.connect(self.sel_eduardo)
        self.cb_uriel.toggled.connect(self.sel_uriel)

        self.badillo = ""
        self.sofia = ""
        self.eduardo = ""
        self.uriel = ""
    # Área de los Slots
    def sel_badillo(self):
        if self.cb_badillo.isChecked():
            print("Badillo True")
            self.badillo = "BADILLO\n"
        else:
            print("Badillo False")
            self.badillo = ""
        self.text_equipo.setPlainText(self.badillo + self.sofia + self.eduardo + self.uriel)
    def sel_sofia(self):
        if self.cb_sofia.isChecked():
            print("Sofia True")
            self.sofia = "SOFIA\n"
        else:
            print("Sofia False")
            self.sofia = ""
        self.text_equipo.setPlainText(self.badillo + self.sofia + self.eduardo + self.uriel)
    def sel_eduardo(self):
        if self.cb_eduardo.isChecked():
            print("Eduardo True")
            self.eduardo = "EDUARDO\n"
        else:
            print("Eduardo False")
            self.eduardo = ""
        self.text_equipo.setPlainText(self.badillo + self.sofia + self.eduardo + self.uriel)
    def sel_uriel(self):
        if self.cb_uriel.isChecked():
            print("Uriel True")
            self.uriel = "URIEL\n"
        else:
            print("Uriel False")
            self.uriel = ""
        self.text_equipo.setPlainText(self.badillo + self.sofia + self.eduardo + self.uriel)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

