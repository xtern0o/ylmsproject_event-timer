import sys
import datetime as dt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from source.ui_generated_py_files.ui_main_menu import Ui_MainWindow
from source.db_class import Db
from source.logs.log_class import Logger
from source.event_widget import EventWidget
from source.event_creator import CreateDialog


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


class MainMenuWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user_id: int, parent=None):
        super().__init__()
        self.user_id = user_id
        self.reg_window = parent  # parent

        self.reg_window.close()

        self.db = Db()
        self.logger = Logger()

        self.widget_list = []

        self.setupUi(self)
        self.username.setText(str(self.db.get_user_data(self.user_id)[1]))

        self.statusbar.setStyleSheet("color: pink;")
        self.setWindowIcon(QIcon("../icons/timer.png"))

        self.load_events_from_db()

        self.logout_btn.clicked.connect(self.logout)
        self.add_btn.clicked.connect(self.create_new)
        self.refresh_btn.clicked.connect(self.update_widget_list)

        self.search_le.textChanged.connect(self.searching)

    def logout(self):
        self.db.set_remembered(self.user_id, False)
        self.reg_window.login_le.setText("")
        self.reg_window.pwd_le.setText("")
        self.reg_window.remember_btn.setChecked(False)

        self.logger.log(f"Пользователь с id={self.user_id} вышел из аккаунта.")

        self.close()

    def load_events_from_db(self):
        data = sorted(list(set(self.db.get_events_from_this_user(self.user_id))),
                      key=lambda widget_info: widget_info[2])
        for row in data:
            w = EventWidget(*row, parent=self)
            self.widget_lt.addWidget(w)
            self.widget_list.append(w)

        self.logger.log(f"События загружены.")

        self.check_validness_of_events()

    def check_validness_of_events(self):
        for event_widget in self.widget_list:
            dt_ = list(map(int, event_widget.form_dt))
            widget_dt = dt.datetime(year=dt_[0], month=dt_[1], day=dt_[2],
                                    hour=dt_[3], minute=dt_[4], second=dt_[5])
            if widget_dt < dt.datetime.today():
                event_widget.fr.setStyleSheet("""
                QLabel#title {
                    color: #a81900;
                    background-color: #602828;
                    border-radius: 20px;
                }
                """)
                event_widget.last = True
                self.logger.log(f"Событие с id={event_widget.id} получило статус истекшего.")

    def create_new(self):
        self.create_win = CreateDialog(self)
        self.create_win.show()

    def update_widget_list(self):
        self.widget_list.clear()
        for i in reversed(range(self.widget_lt.count())):
            self.widget_lt.itemAt(i).widget().deleteLater()
        self.logger.log("Список событий очищен для обновления.")
        self.load_events_from_db()

    def searching(self):
        text = self.sender().text().lower()
        if text:
            data = list(filter(lambda widget: text in widget.name, self.widget_list))
            if data:
                # создаем список из копий виджетов, так как в дальнейшем объекты удаляются
                data_not_deleted = []
                for w in data:
                    new_w = EventWidget(w.id, w.name, w.d_t, w.hex_color, w.owner_id, self)
                    data_not_deleted.append(new_w)

                for i in range(self.widget_lt.count()):
                    self.widget_lt.itemAt(i).widget().deleteLater()
                for w in data_not_deleted:
                    self.widget_lt.addWidget(w)
            else:
                for i in range(self.widget_lt.count()):
                    self.widget_lt.itemAt(i).widget().deleteLater()
                self.statusbar.showMessage("Событий по данному запросу не найдено", 500)
        else:
            self.update_widget_list()

    def closeEvent(self, a0):
        self.db.con.close()
