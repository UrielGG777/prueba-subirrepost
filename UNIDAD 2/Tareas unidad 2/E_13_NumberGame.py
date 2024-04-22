import sys
import random as rd
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_13_NumberGame.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.txtNumber.setInputMask('000')
        self.playerTurn = True

        # Área de los Signals
        self.btnCheck.clicked.connect(self.check)

    # Área de los Slots
    def check(self):
        if self.checkNumber():
            if self.playerTurn:
                n = self.getNumber()
                x = self.getPlayerNumber()
                if n == x:
                    self.resultMessage('You win!')
                else:
                    self.resultMessage('Try again! The number was: {0}'.format(n))
            else:
                n = self.getPlayerNumber()
                x = self.getNumber()
                if n == x:
                    self.resultMessage('You lost... The computer guessed your number')
                else:
                    self.resultMessage('You won! The computer guessed: {0}'.format(x))
            self.changeState()

    def checkNumber(self):
        if self.txtNumber.text() == '':
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Write a number!')
            msgBox.exec_()
            return False
        if int(self.txtNumber.text()) < 0 or int(self.txtNumber.text()) > 100:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText('Pick a number between 0 and 100!')
            msgBox.exec_()
            return False
        return True

    def changeState(self):
        if self.playerTurn:
            self.playerTurn = False
            self.txtNumber.setText('')
            self.lbPrimary.setText('▼▼▼  Pick a number between 1 and 100 ▼▼▼')
        else:
            self.playerTurn = True
            self.txtNumber.setText('')
            self.lbPrimary.setText('!!! The computer has picked a number between 1 and 100, try and guess it !!!')

    def resultMessage(self, text):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.exec_()

    def getNumber(self):
        return rd.randint(1, 100)

    def getPlayerNumber(self):
        return int(self.txtNumber.text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

