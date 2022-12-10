import sys
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QColorDialog
from source.ui_generated_py_files.ui_settings import Ui_MainWindow
from source.db_class import Db
from source.logs.log_class import Logger


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


class SettingWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(959, 295)

        self.db = Db()
        self.logger = Logger()

        self.event_widget = parent

        self.name_le.setText(self.event_widget.name)
        self.color_le.setText(self.event_widget.hex_color)
        self.change_style_sheet(self.event_widget.hex_color)

        self.delete_now.clicked.connect(self.delete_now_f)
        self.color_btn.clicked.connect(self.choose_color)
        self.confirm_btn.clicked.connect(self.confirm)
        self.color_le.textChanged.connect(self.change_color)

    def delete_now_f(self):
        message = 'Вы уверены, что хотите удалить это событие?'
        reply = QMessageBox.question(self, 'Уведомление', message, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            print(self.event_widget.id)
            self.db.delete_event(self.event_widget.id)
            self.event_widget.main_menu.update_widget_list()

            self.logger.log(f"Событие с id={self.event_widget.id} удалено пользователем из окна настроек.")

            self.close()

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

    def confirm(self):
        if self.color_str_is_valid(self.color_le.text()) and len(self.name_le.text()) >= 3:
            self.db.update_event_properties(self.event_widget.id,
                                            self.name_le.text(),
                                            self.color_le.text())
            self.event_widget.main_menu.update_widget_list()

            self.logger.log(f"Событие с id={self.event_widget.id} изменено.\n"
                            f"Новое название: {self.name_le.text()}; новый цвет: {self.color_le.text()}")

            self.close()
        elif not self.color_str_is_valid(self.color_le.text()):
            q = QMessageBox(self)
            q.setObjectName("error_dialog")
            q.critical(self, "Ошибка ", "Проверьте правильность введенного вами цвета.\n"
                                        "При наведении курсора поле ввода должно окраситься"
                                        " в соответствии с этим цветом.\n", QMessageBox.Ok)

            self.logger.log("Некорректный цвет выбран при изменении события.")

        else:
            q = QMessageBox(self)
            q.setObjectName("error_dialog")
            q.critical(self, "Ошибка ", "Длина названия события должна быть более 2 символов.", QMessageBox.Ok)

            self.logger.log("Некорректное названия при изменении события.")
