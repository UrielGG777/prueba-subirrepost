from QLabelClickeable import clickable
import sys

from PyQt5 import uic, QtWidgets, QtCore, QtGui
qtCreatorFile = "P10_ClicImage1.ui"  # Nombre del archivo
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        clickable(self.img).connect(self.clicImage)

        self.btn_borrar.clicked.connect(self.borrar)

    def clicImage(self):
        print("Hiciste clic")
        self.txt_Nombre.setText("Paco")
        self.txt_Edad.setText("6")
        self.txt_Ocupacion.setText("Asesino")


    def borrar(self):
        reply = QtWidgets.QMessageBox.warning(self, "Mensaje", "Seguro que quieres borrar la info?",
                                              QtWidgets.QMessageBox.Yes,
                                              QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:

            self.txt_Nombre.setText("")
            self.txt_Edad.setText("")
            self.txt_Ocupacion.setText("")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("¡¡¡BIENVENIDO!!!")
            resp = msgBox.exec_()
            print("Respuesta: ", resp)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
