import sys
from random import choice as rdchoice
from time import sleep

from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.uic.properties import QtGui

qtCreatorFile = "E_11_HangedGame.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.words = [
            'PURPLE',
            'WINDOW',
            'BASKET',
            'ROCKET',
            'YELLOW',
            'GUITAR',
            'CIRCLE',
            'WALLET',
            'SQUARE',
            'BUTTER',
            'SPIRIT',
            'PLANET',
            'CAMERA',
            'CANDLE',
            'DOCTOR',
            'GARDEN',
            'FINGER',
            'HAMMER',
            'WINTER',
            'ORANGE',
            'CARPET',
            'SHADOW',
            'PILLOW',
            'SILVER',
            'CIRCLE',
            'CORNER',
            'DRAGON',
            'FLOWER',
            'STRONG',
            'BASKET',
            'BANANA',
            'COTTON',
            'TUNNEL',
            'MOTHER',
            'CASTLE',
            'BOTTLE',
            'STATUE',
            'CHERRY',
            'ROCKET',
            'FATHER',
            'PURPLE',
            'SPIDER',
            'CIRCLE',
            'COTTON',
            'GENTLE',
            'BRANCH',
            'GUITAR',
            'FOREST',
            'SPIRIT',
            'YELLOW',
            'RABBIT',
            'PILLOW',
            'GARDEN',
            'BOTTLE',
            'WINDOW',
            'MOTHER',
            'SILVER',
            'WINTER',
            'CIRCLE',
            'PLANET',
            'CANDLE',
            'ROCKET',
            'SHADOW',
            'HAMMER',
            'BUTTER',
            'DRAGON',
            'CAMERA',
            'CHERRY',
            'SQUARE',
            'WALLET',
            'TUNNEL',
            'PURPLE',
            'CIRCLE',
            'CORNER',
            'ORANGE',
            'BASKET',
            'GARDEN',
            'WINTER',
            'DOCTOR',
            'BOTTLE',
            'FINGER',
            'SPIRIT',
            'ROCKET',
            'WINDOW',
            'DRAGON',
            'ROCKET',
            'PLANET',
            'GUITAR',
            'SILVER',
            'CIRCLE',
            'CASTLE',
            'COTTON',
            'CHERRY',
            'DOCTOR',
            'PURPLE',
            'WALLET',
            'RABBIT',
            'CANDLE',
            'HAMMER',
            'TUNNEL',
        ]
        self.choosenWord = []
        self.check = [0, 0, 0, 0, 0, 0]
        self.initialize()
        self.stage = 0

        # Área de los Signals
        self.btnA.clicked.connect(self.checkLetter)
        self.btnB.clicked.connect(self.checkLetter)
        self.btnC.clicked.connect(self.checkLetter)
        self.btnD.clicked.connect(self.checkLetter)
        self.btnE.clicked.connect(self.checkLetter)
        self.btnF.clicked.connect(self.checkLetter)
        self.btnG.clicked.connect(self.checkLetter)
        self.btnH.clicked.connect(self.checkLetter)
        self.btnI.clicked.connect(self.checkLetter)
        self.btnJ.clicked.connect(self.checkLetter)
        self.btnK.clicked.connect(self.checkLetter)
        self.btnL.clicked.connect(self.checkLetter)
        self.btnM.clicked.connect(self.checkLetter)
        self.btnN.clicked.connect(self.checkLetter)
        self.btnO.clicked.connect(self.checkLetter)
        self.btnP.clicked.connect(self.checkLetter)
        self.btnQ.clicked.connect(self.checkLetter)
        self.btnR.clicked.connect(self.checkLetter)
        self.btnS.clicked.connect(self.checkLetter)
        self.btnT.clicked.connect(self.checkLetter)
        self.btnU.clicked.connect(self.checkLetter)
        self.btnV.clicked.connect(self.checkLetter)
        self.btnW.clicked.connect(self.checkLetter)
        self.btnX.clicked.connect(self.checkLetter)
        self.btnY.clicked.connect(self.checkLetter)
        self.btnZ.clicked.connect(self.checkLetter)

    # Área de los Slots
    def checkLetter(self):
        try:
            self.sender().setEnabled(False)
            letter = self.sender().text()
            positions = self.findPositions(letter=letter)
            if positions:
                for position in positions:
                    lb = getattr(self, f'lb{position}')
                    lb.setText(letter)
                    self.check[position] = 1
                    if all(element == 1 for element in self.check):
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText('Game Won!')
                        msgBox.exec_()
                        QApplication.quit()
            else:
                self.stage += 1
                pixmap = QPixmap(':/Otro/Hanged{0}.png'.format(self.stage))
                self.lbHanged.setPixmap(pixmap)
                if self.stage == 7:
                    for i in range(0, 6):
                        lb = getattr(self, f'lb{i}')
                        lb.setText(self.choosenWord[i])
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText('Game Ovah')
                    msgBox.exec_()
                    QApplication.quit()
        except Exception as e:
            print(e)


    def initialize(self):
        self.choosenWord = list(rdchoice(self.words))

    def findPositions(self, letter):
        positions = []
        for i, c in enumerate(self.choosenWord):
            if c == letter:
                positions.append(i)
        return positions


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

