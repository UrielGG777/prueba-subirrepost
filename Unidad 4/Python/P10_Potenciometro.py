import serial
import sys
from PyQt5 import uic, QtWidgets, QtGui,  QtCore
qtCreatorFile = "P10_Potenciometro.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.lecturaArduino)
        self.arduino = None

        self.btnconectar.clicked.connect(self.conexion)

    def conexion(self):
        com = self.txt_com.text()
        if self.arduino is None or not self.arduino.isOpen():
            try:
                self.arduino = serial.Serial(port=com, baudrate=9600, timeout=1)
                self.segundoPlano.start(100)
                self.textEdit.setText("CONEXION EXITOSA")
                self.btnconectar.setText("DESCONECTAR")
            except serial.SerialException as e:
                    self.textEdit.setText("ERROR DE CONEXION: " + str(e))
            else:
                self.arduino.close()
                self.segundoPlano.stop()
                self.textEdit.setText("DESCONECTADO EXITOSAMENTE")
                self.btnconectar.setText("CONECTAR")

    def lecturaArduino(self):
            if not self.arduino is None and self.arduino.isOpen():
                if self.arduino.inWaiting():
                    cadena = self.arduino.readline()
                    cadena = cadena.decode()
                    cadena = cadena.strip()
            if cadena != "":
                    self.datos.addItem(cadena)
                    self.datos.setCurrentRow(self.datos.count()-1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
