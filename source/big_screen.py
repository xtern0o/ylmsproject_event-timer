import sys
import datetime as dt
import threading
from time import sleep
from source.minions_easter import Minion
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from source.ui_generated_py_files.ui_timer_screen import Ui_MainWindow
from source.logs.log_class import Logger
from PyQt5.QtCore import QPoint


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


# special thanks to the stackoverflow user with nickname Shawn Chin
def strfdelta(tdelta: dt.timedelta, fmt: str):
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)


class BigScreen(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.logger = Logger()

        self.event_widget = parent
        self.set_color(self.event_widget.hex_color)

        self.event_name_lbl.setText(str(self.event_widget.name))
        self.statusbar.showMessage("[F], чтобы переключить полноэкранный режим,"
                                   " [ESC], чтобы выйти." 
                                   " Перемещайте виджет мышкой"
                                   " Попробуйте конпки [X], [Z]", 10000)
        self.setWindowIcon(QIcon("../icons/timer.png"))

        dt_ = list(map(int, self.event_widget.form_dt))
        self.target_date_time = dt.datetime(year=dt_[0], month=dt_[1], day=dt_[2],
                                            hour=dt_[3], minute=dt_[4], second=dt_[5])

        self.thread_running = True
        self.big_screen_timer = threading.Thread(target=self.change_value,
                                                 daemon=True)
        self.logger.log(f"Для события с id={self.event_widget.id} открыт таймер.\n"
                        f"Он работает в потоке {self.big_screen_timer.name}")
        self.big_screen_timer.start()

    def keyPressEvent(self, event):
        # Toggle full screen mode
        if event.key() == Qt.Key_F:
            if self.isFullScreen():
                self.showNormal()
                self.logger.log("Для таймера включен полноэкранный режим")
            else:
                self.logger.log("Для таймера выключен полноэкранный режим")
                self.showFullScreen()

        elif event.key() == Qt.Key_Escape:
            self.logger.log(f"Таймер события с id={self.event_widget.id} закрыт.")
            self.close()

        elif event.key() == Qt.Key_K:
            self.logger.log("Это всё миньоны")
            self.easter = Minion()
            self.easter.show()

        elif event.key() == Qt.Key_X:
            current_opacity = self.windowOpacity()
            current_opacity -= 0.2
            if current_opacity <= 0:
                current_opacity = 1
            self.setWindowOpacity(current_opacity)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            if not self.isFullScreen():
                delta = QPoint(event.globalPos() - self.oldPos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPos()
        except AttributeError:
            pass

    def set_color(self, color):
        self.event_name_lbl.setStyleSheet(f"""
                QLabel#event_name_lbl {{
                    font-family: Verdana, Geneva, sans-serif;
                    font-size: 40px;
                    letter-spacing: 2px;
                    word-spacing: 6px;
                    color: {color};
                    font-variant: small-caps;
                    text-transform: lowercase;
                    border-radius: 20px;
                }}
                QLabel#event_name_lbl:hover {{
                    color: #F3E0D2;
                }}
                """)
        self.frame_2.setStyleSheet(f"""
            QFrame#frame_2 {{
                background-color: #040c0e;
                border: 2px solid {color};
                border-radius: 20px;
            }}
                """)
        self.statusbar.setStyleSheet("color: pink")

    def change_value(self):
        while True:
            if self.thread_running:
                current_datetime = dt.datetime.today()
                delta = self.target_date_time - current_datetime

                self.days_lbl.setText("days: " + str(delta.days))
                self.hms_lbl.setText(strfdelta(delta, "{hours} : {minutes} : {seconds}"))

                sleep(0.2)

                if delta.seconds <= 30:
                    self.hms_lbl.setStyleSheet("""
                    QLabel#hms_lbl {
                        color: #a81900;
                    }
                    """)

                elif self.target_date_time <= current_datetime:
                    print('aaa')
                    self.thread_running = False
                    self.logger.log(f"Событие с id={self.event_widget.id} окончено.")
                    self.event_widget.main_menu.check_validness_of_events()
            else:
                return None

    def closeEvent(self, event):
        self.event_widget.is_opened = False


