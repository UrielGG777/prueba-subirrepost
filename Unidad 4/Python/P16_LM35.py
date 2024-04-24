import serial
import sys
from PyQt5 import uic, QtWidgets, QtCore
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

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.mostrar_temperaturas)
        self.timer.start(1000)  # Se ejecutará cada segundo

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

    def mostrar_temperaturas(self):
        if self.arduino and self.arduino.isOpen():
            # Leer la línea del puerto serial
            lectura = self.arduino.readline().decode().strip()
            valores = lectura.split(",")  # Separar los valores por la coma

            if len(valores) == 2:  # Asegurarse de que haya recibido dos valores
                temp1, temp2 = valores  # Asignar los valores a temp1 y temp2

                # Mostrar los valores en los QLineEdit
                self.txt_lm35.setText(temp1)
                self.txt_temperatura.setText(temp2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())