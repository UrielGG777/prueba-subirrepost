import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P_04_OpenAritmetica.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_resta.clicked.connect(self.resta)
        self.btn_Multiplicar.clicked.connect(self.Multiplicar)
        self.btn_Division.clicked.connect(self.Division)
        self.txt_resultado.setEnabled (False)
    # Área de los Slots
    def sumar(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A+B
        self.txt_resultado.setText(str(r))

    def resta(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A - B
        self.txt_resultado.setText(str(r))
    def Multiplicar(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A * B
        self.txt_resultado.setText(str(r))
    def Division(self):
        A = int(self.txt_A.text())
        B = int(self.txt_B.text())
        r = A / B
        self.txt_resultado.setText(str(r))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

