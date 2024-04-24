import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P13_LED_conexionConGUI.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None

        self.btn_led.clicked.connect(self.estadoLed)

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

    def estadoLed(self):
        if not self.arduino is None and self.arduino.isOpen():
            if self.estado_led == 0:
                # Cambiar el texto del botón a "PRENDER"
                self.btn_control_led.setText("PRENDER")
                # Enviar el comando al Arduino para encender el LED
                self.arduino.write('1'.encode())
            else:
                # Cambiar el texto del botón a "APAGAR"
                self.btn_control_led.setText("APAGAR")
                # Enviar el comando al Arduino para apagar el LED
                self.arduino.write('0'.encode())
            # Alternar el estado del LED


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())