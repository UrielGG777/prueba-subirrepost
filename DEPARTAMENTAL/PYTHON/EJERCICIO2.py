import sys
import serial
from PyQt5 import uic, QtGui, QtWidgets, QtCore

# Load the UI file
qtCreatorFile = "EJERCICIO2.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.conexion = -1
        self.arduino = None

        # Timer for reading from Arduino
        self.QtTimer = QtCore.QTimer()
        self.QtTimer.timeout.connect(self.lecturaArduino)
        self.QtTimer.setInterval(1000)

        # Connect button click to the connection handler
        self.btn_conec_desco.clicked.connect(self.conexionArduino)

    def conexionArduino(self):
        try:
            if self.conexion == -1:
                self.arduino = serial.Serial(port='com4', baudrate=9600, timeout=10)
                self.btn_conec_desco.setText("Desconectar")
                self.conexion = 1
                self.QtTimer.start()
            elif self.conexion == 0:
                self.arduino.open()
                self.btn_conec_desco.setText("Desconectar")
                self.conexion = 1
                self.QtTimer.start()
            elif self.conexion == 1:
                self.arduino.close()
                self.btn_conec_desco.setText("Conectar")
                self.conexion = 0
                self.QtTimer.stop()
        except serial.SerialException as e:
            print(f"Error : {e}")

    def lecturaArduino(self):
        if self.arduino and self.arduino.isOpen():
            try:
                lectura = self.arduino.readline().decode().strip()
                if lectura:
                    self.lbl_movimiento.setText(lectura)
            except serial.SerialException as e:
                print(f"Error : {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
