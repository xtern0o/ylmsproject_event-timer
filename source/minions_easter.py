import sys
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

SIZE_POLICY = (500, 100, 1000, 1000)


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


class Minion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(*SIZE_POLICY)
        self.setWindowTitle("WOOW")

        img = QLabel(self)
        img.resize(2000, 1000)
        img.setPixmap(QPixmap("minions.jpg"))

