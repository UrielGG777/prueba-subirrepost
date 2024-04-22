import sys
import random
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap

qtCreatorFile = "E1_PiedraPapelTijeras.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.opciones_juego = {
            1: ["Piedra", ":/Variadas/Imagenes/Piedra.png"],
            2: ["Papel", ":/Variadas/Imagenes/Papel.png"],
            3: ["Tijeras", ":/Variadas/Imagenes/Tijeras.png"]
        }

        self.comboBox.addItem("Piedra", 1)
        self.comboBox.addItem("Papel", 2)
        self.comboBox.addItem("Tijeras", 3)

        self.comboBox.currentIndexChanged.connect(self.seleccionUsuario)
        self.btn_jugar.clicked.connect(self.jugar)
        self.opcion_seleccionada = None
        self.opcion_seleccionada_maquina = None

    # Área de los Slots
    def seleccionUsuario(self):
        dataClave = self.comboBox.currentData()
        self.opcion_seleccionada=dataClave
        imagen = self.opciones_juego[dataClave][-1]
        self.Img_seleccionado.setPixmap(QtGui.QPixmap(imagen))
        print(self.opcion_seleccionada)
        return self.opcion_seleccionada

    def jugar(self):
        opcion_aleatoria = random.choice(list(self.opciones_juego.keys()))
        self.opcion_seleccionada_maquina=opcion_aleatoria
        imagen_aleatoria = self.opciones_juego[opcion_aleatoria][-1]
        self.Img_computadora.setPixmap(QtGui.QPixmap(imagen_aleatoria))
        self.definirganador()

    def definirganador(self):
        opcion_usuario = self.seleccionUsuario()
        opcion_maquina = self.opcion_seleccionada_maquina

        resultado = ""

        if opcion_usuario == opcion_maquina:
            resultado = "Empate"
        elif (opcion_usuario == 1 and opcion_maquina == 2):
            resultado = "Perdiste"
        elif (opcion_usuario == 1 and opcion_maquina == 3):
            resultado = "Ganaste"
        elif (opcion_usuario == 2 and opcion_maquina == 1):
            resultado = "Ganaste"
        elif (opcion_usuario == 2 and opcion_maquina == 3):
            resultado = "Perdiste"
        elif (opcion_usuario == 3 and opcion_maquina == 1):
            resultado = "Perdiste"
        elif (opcion_usuario == 3 and opcion_maquina == 2):
            resultado = "Ganaste"
        else:
            resultado = "Error"

        self.txt_resultado.setText(resultado)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

