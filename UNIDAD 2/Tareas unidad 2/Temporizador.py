import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer


class TemporizadorApp(QMainWindow):
    def __init__(self):
        super(TemporizadorApp, self).__init__()
        loadUi("temporizador.ui", self)

        self.iniciar_btn.clicked.connect(self.iniciar_temporizador)

    def iniciar_temporizador(self):
        segundos = self.segundos_spinbox.value()
        self.contador = segundos
        self.actualizar_label()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_temporizador)
        self.timer.start(1000)

    def actualizar_temporizador(self):
        self.contador -= 1
        self.actualizar_label()
        if self.contador == 0:
           self.timer.stop()
           self.label.setText("¡Tiempo terminado!")

    def actualizar_label(self):
        self.label.setText(f"Tiempo restante: {self.contador} segundos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TemporizadorApp()
    ventana.show()
    sys.exit(app.exec_())



