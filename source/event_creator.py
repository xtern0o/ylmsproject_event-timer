import sys
from PyQt5.QtWidgets import QDialog, QColorDialog, QMessageBox
from PyQt5.Qt import QDateTime
from source.ui_generated_py_files.ui_create_event_dialog import Ui_Dialog
from source.db_class import Db
from source.logs.log_class import Logger


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


class CreateDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(710, 200)
        self.setWindowTitle("Создание нового события")

        self.dateTime_ed.setDateTime(QDateTime.currentDateTime())
        self.dateTime_ed.setMinimumDateTime(QDateTime.currentDateTime())

        self.db = Db()
        self.logger = Logger()

        self.parent = parent
        self.color = self.color_le.text()

        self.color_btn.clicked.connect(self.choose_color)
        self.create_btn.clicked.connect(self.add_new_event)

        self.color_le.textChanged.connect(self.change_color)

    def choose_color(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.color = col.name()
            self.color_le.setText(col.name())
            self.change_style_sheet(col.name())

    def change_color(self):
        col = self.color_le.text()
        if self.color_str_is_valid(col):
            self.change_style_sheet(col)
            self.color = col

    def change_style_sheet(self, color: str):
        self.color_le.setStyleSheet(f"""
            QLineEdit {{
                background-color: #525b56;
                color: #a4978e;
                border-radius: 10px;
                font-family: Verdana, Geneva, sans-serif;
                font-size: 20px;
                letter-spacing: 2px;
                word-spacing: 6px;
            }}
            QLineEdit:hover {{
                background-color: {color};
                color: #132226;
                opacity: 1;
            }}
            """)

    def color_str_is_valid(self, color):
        try:
            return len(color) == 7 and color[0] == "#"
        except IndexError:
            return False

    def add_new_event(self):
        if self.color_str_is_valid(self.color_le.text()) and len(self.event_name_le.text()) >= 3:
            ymd = self.dateTime_ed.dateTime().toString("yyyy-MM-dd")
            smh = self.dateTime_ed.dateTime().toString("hh:mm")
            self.db.add_event(self.event_name_le.text(),
                              ymd + " " + smh,
                              self.color_le.text(),
                              self.parent.user_id)
            self.parent.update_widget_list()

            self.logger.log(f"Новое событие {self.event_name_le.text()}"
                            f" с пометкой цвета {self.color_le.text()} успешно создано;\n"
                            f"Запланированная дата - {ymd} {smh}")

            self.close()
        elif not self.color_str_is_valid(self.color_le.text()):
            q = QMessageBox(self)
            q.setObjectName("error_dialog")
            q.critical(self, "Ошибка ", "Проверьте правильность введенного вами цвета.\n"
                                        "При наведении курсора поле ввода должно окраситься"
                                        " в соответствии с этим цветом.\n", QMessageBox.Ok)

            self.logger.log("Некорректный цвет выбран при создании события.")

        else:
            q = QMessageBox(self)
            q.setObjectName("error_dialog")
            q.critical(self, "Ошибка ", "Длина названия события должна быть более 2 символов.", QMessageBox.Ok)

            self.logger.log("Некорректное названия при создании события.")


