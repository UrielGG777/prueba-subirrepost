import math
import random
import serial
import sys
from PyQt5 import QtWidgets, QtCore
import Plantilla_juegoV2 as grafica
import matplotlib.pyplot as plt
from PyQt5.QtGui import QColor

class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuración
        self.btn_action.clicked.connect(self.action)
        self.btn_action.clicked.connect(self.control_temporizador)
        self.btn_arriba.clicked.connect(self.arriba)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_abajo.clicked.connect(self.abajo)
        self.btn_reiniciar.clicked.connect(self.reiniciar_juego)
        self.perdida = False
        self.score = 0

        # Configuración del timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.timeout.connect(self.upScore)
        self.timer.timeout.connect(self.sendDistance)
        self.timer.setInterval(1000)
        self.time = 60

        # Configuración del timer de movimiento del enemigo
        self.movimiento_enemigo_timer = QtCore.QTimer(self)
        self.movimiento_enemigo_timer.timeout.connect(self.movimiento_enemigo)
        self.movimiento_enemigo_timer.setInterval(3000)
        self.enemyTimer = 0

        self.puntaje = 0  # Inicializar puntaje

        self.xMax = 5
        self.xMin = -5
        self.yMax = 5
        self.yMin = -5
        self.deshabilitar_botones()

        self.personajes = [[0, 0], [0, 0], [0, 0], [0, 0]] # Jugador y Computadora
        self.limpiar()

        # Configuración del color del personaje
        self.color_personaje = "green"

        self.btn_action.setEnabled(False)
        # Conectar la señal de cambio de índice del combo box
        combo_color = self.colorPicker.findChild(QtWidgets.QComboBox, "combo_color")
        combo_color.currentIndexChanged.connect(self.actualizar_color_personaje)

        self.arduino = serial.Serial(port='com4', baudrate=9600, timeout=1)

    #Area de los Slots
    def sendDistance(self):
        try:
            minDistance = 1000
            for i in range(1, len(self.personajes)):
                tempDistance = math.sqrt(math.pow(self.personajes[0][0] - self.personajes[i][0], 2) + math.pow(
                    self.personajes[0][1] - self.personajes[i][1], 2))
                minDistance = tempDistance if tempDistance < minDistance else minDistance
                cadena = "S"
                if minDistance > 5:
                    cadena += "0"
                if minDistance > 2:
                    cadena += "1"
                if minDistance > 0:
                    cadena += "2"
                self.arduino.write(cadena.encode())
        except Exception as e:
            print(e)

    def showTime(self):
        self.contadorLCD.display(self.time)
        self.time -= 1
        if self.time < 0:
            self.timer.stop()
            QtWidgets.QMessageBox.warning(self, "Advertencia", "¡Se ha terminado el tiempo!")
            self.timer.stop()
            self.puntuacion.setText("")
            self.btn_action.setText("INICIAR")
            self.limpiar()

    def upScore(self):
        self.score += 1
        self.puntuacion.setText(str(self.score))

    def upScoreEnemy(self):
        self.score += 100
        self.puntuacion.setText(str(self.score))

    def cuenta(self):
        self.time = 60
        self.timer.start()

    def detener(self):
        self.timer.stop()

    def control_temporizador(self):
        try:
            if self.btn_action.text() == "DETENER":
                self.cuenta()
            else:
                self.timer.stop()
        except Exception as e:
            print(e)

    def deshabilitar_botones(self):
        self.btn_arriba.setEnabled(False)
        self.btn_izquierda.setEnabled(False)
        self.btn_derecha.setEnabled(False)
        self.btn_abajo.setEnabled(False)

    def habilitar_botones(self):
        self.btn_arriba.setEnabled(True)
        self.btn_derecha.setEnabled(True)
        self.btn_abajo.setEnabled(True)
        self.btn_izquierda.setEnabled(True)

    def action(self):
        if self.btn_action.text() == "INICIAR":
            self.btn_action.setText("DETENER")
            self.habilitar_botones()
            self.personajes[0] = [0, 0] # Vuelve al jugador al centro

            for i in range(1, len(self.personajes)):
                self.personajes[i] = [random.randrange(self.xMin, self.xMax),
                                      random.randrange(self.yMin, self.yMax)]  # Posición aleatoria para la computadora

            self.graficar()
            self.movimiento_enemigo_timer.start()
            self.arduino.write("T3".encode())
        else:
            self.btn_action.setText("INICIAR")
            self.deshabilitar_botones()
            self.limpiar()
            self.movimiento_enemigo_timer.stop()

    def movimiento_enemigo(self):
        try:
            for i in range(1, len(self.personajes)):

                movimiento_x = random.choice([-1, 0, 1])
                movimiento_y = random.choice([-1, 0, 1])

                nueva_posicion_x = self.personajes[i][0] + movimiento_x
                nueva_posicion_y = self.personajes[i][1] + movimiento_y
                if self.xMin <= nueva_posicion_x <= self.xMax and self.yMin <= nueva_posicion_y <= self.yMax:
                    self.personajes[i] = [nueva_posicion_x, nueva_posicion_y]
                else:
                    self.personajes[i] = [random.randrange(self.xMin, self.xMax),
                                          random.randrange(self.yMin, self.yMax)]
                self.verificar_perdida()
            self.limpiar()
            self.graficar()
        except Exception as e:
            print(e)


    def arriba(self):
        if self.personajes[0][1] < self.yMax:
            self.personajes[0][1] += 1
            self.limpiar()
            self.graficar()
            self.verificar_ganador()
            self.verificar_perdida()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "¡No puedes salirte de los límites!")

    def izquierda(self):
        if self.personajes[0][0] > self.xMin:
            self.personajes[0][0] -= 1
            self.limpiar()
            self.graficar()
            self.verificar_ganador()
            self.verificar_perdida()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "¡No puedes salirte de los límites!")

    def derecha(self):
        if self.personajes[0][0] < self.xMax:
            self.personajes[0][0] += 1
            self.limpiar()
            self.graficar()
            self.verificar_ganador()
            self.verificar_perdida()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "¡No puedes salirte de los límites!")

    def abajo(self):
        if self.personajes[0][1] > self.yMin:
            self.personajes[0][1] -= 1
            self.limpiar()
            self.graficar()
            self.verificar_ganador()
            self.verificar_perdida()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "¡No puedes salirte de los límites!")

    def limpiar(self):
        plt.cla()
        x = [i for i in range(self.xMin, self.xMax + 1)]
        y = [i for i in range(self.yMin, self.yMax + 1)]
        self.ax.set_xticks(x)
        self.ax.set_yticks(y)
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)
        self.canvas.draw()

    def graficar(self):
        try:
            self.ax.plot(self.personajes[0][0], self.personajes[0][1],
                         marker="x", markersize=8, color=self.color_personaje)

            for i in range(1, len(self.personajes)):
                self.ax.plot(self.personajes[i][0], self.personajes[i][1],
                             marker="o", markersize=8, markerfacecolor="green", markeredgewidth=1,
                             markeredgecolor="black")

            self.canvas.draw()
        except Exception as e:
            print(e)

    def verificar_ganador(self):
        try:
            for i in range(1, len(self.personajes)):
                if self.personajes[0] == self.personajes[i]:
                    self.upScoreEnemy()
                    self.personajes.pop(i)
                    cadena = "T"+str(len(self.personajes)-1)
                    self.arduino.write(cadena.encode())
                    self.timer.start()
                    if len(self.personajes) == 1:
                        QtWidgets.QMessageBox.information(self, "Juego Terminado",
                                                          "¡Has derrotado a todos los enemigos!")
                        self.btn_action.setText("INICIAR")
                        self.deshabilitar_botones()
                        self.btn_reiniciar.setEnabled(True)
                    else:
                        self.btn_action.setText("INICIAR")
        except Exception as e:
            print(e)

    def verificar_perdida(self):
        for i in range(1, len(self.personajes)):
            if self.personajes[0] == self.personajes[i]:
                QtWidgets.QMessageBox.information(self, "Juego Terminado", "¡Has sido derrotado por el enemigo!")
                self.limpiar()
                self.btn_action.setText("INICIAR")
                self.deshabilitar_botones()
                self.reiniciar_juego()
                self.perdida = True
                return
    def reiniciar_juego(self):
        self.puntaje = 0
        self.personajes = [[0, 0], [0, 0], [0, 0], [0, 0]]
        self.time = 60
        self.limpiar()
        self.graficar()
        self.timer.stop()
        self.movimiento_enemigo_timer.stop()
        self.btn_action.setText("INICIAR")
        self.deshabilitar_botones()  #
        self.btn_reiniciar.setEnabled(False)
        self.perdida = False

    def actualizar_color_personaje(self):
        color_seleccionado = self.colorPicker.findChild(QtWidgets.QComboBox, "combo_color").currentText()

        if color_seleccionado == "Rojo":
            self.color_personaje = "red"
        elif color_seleccionado == "Amarillo":
            self.color_personaje = "yellow"
        elif color_seleccionado == "Azul":
            self.color_personaje = "blue"

        self.btn_action.setEnabled(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())