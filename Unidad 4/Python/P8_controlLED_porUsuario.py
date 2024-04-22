import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P8_controlLED_porUsuario.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.arduino = None

        self.btnapagar_prender.clicked.connect(self.apagar_prender)
        self.estado_led = 0


    # Area de Slots
    def apagar_prender(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.estado_led == 0:
                self.arduino.write(b'1')#representa un byte pero en python, quiere decir interpretara si el led esta prendido o apagado
                self.datos.append("LED encendido")
                self.btnapagar_prender.setText("PRENDER")
            else:
                self.arduino.write(b'0')
                self.datos.append("LED apagado")
                self.btnapagar_prender.setText("APAGAR")
            self.estado_led = self.estado_led * -1

    #Area de Slots
    def accion(self):
        texto_boton = self.btn_accion.text()
        com = self.txt_com.text()
        if texto_boton == "CONECTAR" and self.arduino is None:
            self.arduino = serial.Serial(port=com, baudrate=9600, timeout=10)
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")
        elif texto_boton == "DESCONECTAR" and self.arduino.isOpen():
            self.segundoPlano.stop()
            self.arduino.close()
            self.btn_accion.setText("RECONECTAR")
        else:
            self.arduino.open()
            self.segundoPlano.start(100)
            self.btn_accion.setText("DESCONECTAR")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())