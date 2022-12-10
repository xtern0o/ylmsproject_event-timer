import sys
from source.reg_window import RegWindow
from PyQt5.QtWidgets import QApplication


def except_hook(c, e, t):
    return sys.__excepthook__(c, e, t)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = RegWindow()
    win.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
