import serial
import sys
import time
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

qtCreatorFile = "P14_MaquinaEstados_SumaNumeros.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_accion.clicked.connect(self.accion)
        self.arduino = None
        self.btn_enviar.clicked.connect(self.enviar_valores)

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

    def enviar_valores(self):
        if self.arduino is not None and self.arduino.isOpen():
            valorA = self.txt_valorA.text()
            valorB = self.txt_valorB.text()
            self.arduino.write(valorA.encode())
            time.sleep(2)
            self.arduino.write(valorB.encode())
            respuesta = self.arduino.readline().decode().strip()
            QMessageBox.information(self, "Resultado", f"Resultado: {respuesta}")
            self.preguntar_repetir()
        else:
            QMessageBox.warning(self, "Error", "Arduino no está conectado.")

    def preguntar_repetir(self):
        repetir = QMessageBox.question(self, "Repetir proceso", "¿Desea repetir el proceso?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if repetir == QMessageBox.Yes:
            self.txt_valorA.clear()
            self.txt_valorB.clear()
            self.arduino.write('1'.encode())
        else:
            self.arduino.write('0'.encode())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())