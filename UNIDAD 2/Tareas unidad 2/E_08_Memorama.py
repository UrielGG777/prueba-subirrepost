import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import random

from PyQt5.QtCore import QTimer

qtCreatorFile = "E08_Memorama.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.buttons = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                        self.pushButton_5, self.pushButton_6, self.pushButton_7, self.pushButton_8,
                        self.pushButton_9, self.pushButton_10, self.pushButton_11, self.pushButton_12,
                        self.pushButton_13, self.pushButton_14, self.pushButton_15, self.pushButton_16]

        self.tablero = []
        self.pares_encontrados = 0
        self.intentos = 0

        for btn in self.buttons:
            btn.clicked.connect(self.revelar_carta)
            btn.setDisabled(True)
            btn.setIcon(QtGui.QIcon(':/meme/Imagen/como.jpg'))
            btn.setIconSize(QtCore.QSize(150, 150))

        QTimer.singleShot(1000, self.iniciar_juego)

    def iniciar_juego(self):
        imagenes = [':/meme/Imagen/Ardilla.jpeg', ':/meme/Imagen/LEON.jpeg', ':/meme/Imagen/OSO.jpeg',
                    ':/meme/Imagen/URON.jpg',
                    ':/meme/Imagen/VENADO.jpg', ':/meme/Imagen/delfin.jpeg', ':/meme/Imagen/TUCAN.jpg',
                    ':/meme/Imagen/jaguar.jpeg']
        cartas = imagenes * 2
        random.shuffle(cartas)
        self.tablero = [cartas[i:i + 4] for i in range(0, 16, 4)]

        for btn in self.buttons:
            btn.setEnabled(True)

    def revelar_carta(self):
        boton = self.sender()
        index = self.buttons.index(boton)
        fila = index // 4
        columna = index % 4
        carta = self.tablero[fila][columna]

        boton.setIcon(QtGui.QIcon(carta))
        boton.setEnabled(False)

        if not hasattr(self, 'carta_anterior'):
            self.carta_anterior = (fila, columna)
        else:
            fila_ant, columna_ant = self.carta_anterior
            if self.tablero[fila_ant][columna_ant] == carta:
                self.pares_encontrados += 1
                if self.pares_encontrados == 8:
                    self.finalizar_juego()
            else:
                QTimer.singleShot(1000, lambda: self.ocultar_cartas(fila, columna, fila_ant, columna_ant))

            delattr(self, 'carta_anterior')

        self.intentos += 1

    def ocultar_cartas(self, fila1, columna1, fila2, columna2):
        self.buttons[fila1 * 4 + columna1].setIcon(QtGui.QIcon(':/meme/Imagen/como.jpg'))
        self.buttons[fila1 * 4 + columna1].setEnabled(True)
        self.buttons[fila2 * 4 + columna2].setIcon(QtGui.QIcon(':/meme/Imagen/como.jpg'))
        self.buttons[fila2 * 4 + columna2].setEnabled(True)

    def finalizar_juego(self):
        for btn in self.buttons:
            btn.setDisabled(True)

        print(f"Felicidades, ¡completaste el juego en {self.intentos} intentos!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

