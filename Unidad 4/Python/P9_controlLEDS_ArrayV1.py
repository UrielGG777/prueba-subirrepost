import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P9_controlLEDS_ArrayV1.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None

        # Área de los Signals
        self.btn_1.clicked.connect(self.funcion)
        self.btn_2.clicked.connect(self.funcion)
        self.btn_3.clicked.connect(self.funcion)
        self.btn_4.clicked.connect(self.funcion)
        self.btn_5.clicked.connect(self.funcion)
        self.btn_6.clicked.connect(self.funcion)
        self.btn_7.clicked.connect(self.funcion)
        self.btn_8.clicked.connect(self.funcion)

        self.btn_accion.clicked.connect(self.accion)


    #Area de Slots

    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.btn_accion.setText("DESCONECTAR")
    def funcion(self, idx_led):
        if self.arduino is not None and self.arduino.isOpen():
            self.sender.text()
            val = "1" if self.estado_led == 1 else "0" + "\n"
            print(val)
            self.arduino.write(val.encode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
