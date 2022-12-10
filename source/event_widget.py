import sys
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtGui
from source.big_screen import BigScreen
from source.db_class import Db
from source.logs.log_class import Logger
from source.ui_generated_py_files.ui_time_widget import Ui_Form
from source.settings import SettingWindow


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


class EventWidget(QWidget, Ui_Form):
    def __init__(self, id: int,  event_name: str, target_datetime: str, hex_color: str, user_id: int, parent=None):
        super().__init__()
        self.setupUi(self)

        self.main_menu = parent
        self.id = id
        self.name = event_name
        self.hex_color = hex_color
        self.owner_id = user_id
        self.d_t = target_datetime

        self.is_opened = False

        self.db = Db()
        self.logger = Logger()

        self.last = False

        self.form_dt = target_datetime.split(" ")
        self.form_dt.extend(self.form_dt[0].split("-"))
        self.form_dt.extend(self.form_dt[1].split(":"))
        self.form_dt = self.form_dt[2:] + ["00"]

        self.title.setText(str(self.name))
        self.time_ymd_2.setText(" / ".join(self.form_dt[:3]))
        self.time_hms_2.setText(" : ".join(self.form_dt[3:]))

        self.color_frame.setStyleSheet("background-color: {}".format(self.hex_color))

        self.settings_btn_2.clicked.connect(self.open_settings)

    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None:
        if not self.last and not self.is_opened:
            self.big_screen = BigScreen(self)
            self.is_opened = True
            self.big_screen.show()
        elif self.last:
            self.db.delete_event(self.id)
            self.logger.log(f"Событие с id={self.id} удалено из меню.")
            self.close()
            self.main_menu.statusbar.showMessage("Событие {} (id={}) удалено.".format(self.name, self.id), 3000)

    def open_settings(self):
        self.settings = SettingWindow(self)
        self.settings.show()

