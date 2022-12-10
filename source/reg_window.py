import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from source.ui_generated_py_files.ui_reg_window import Ui_MainWindow
from source.main_window import MainMenuWindow as MainWindow
from source.db_class import Db
from source.logs.log_class import Logger


def except_hook(c, e, t):
    sys.__excepthook__(c, e, t)


def password_small_validation(pwd: str) -> bool:
    return len(pwd) > 6


def login_small_validation(login: str) -> bool:
    return len(login) > 3


class RegWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.db = Db()
        self.logger = Logger()

        self.setupUi(self)
        self.setWindowIcon(QIcon("../icons/authoriz.png"))
        self.statusbar.setStyleSheet("color: pink")

        self.check_remember()

        self.enter_btn.clicked.connect(self.login)
        self.register_btn.clicked.connect(self.reg)

    def check_remember(self):
        data = self.db.find_remembered_user()
        if data:
            self.login_le.setText(str(data[1]))
            self.pwd_le.setText(str(data[2]))
            self.remember_btn.setChecked(True)
        self.last_user_id = data[0] if data else None

    def login(self):
        user_id = self.db.get_userid_if_correct_pwd(self.login_le.text(), self.pwd_le.text())
        if user_id:
            if self.last_user_id is not None:
                self.db.set_remembered(self.last_user_id, False)
            self.db.set_remembered(user_id, self.remember_btn.isChecked())

            self.logger.log(f"Пользователь c id={user_id} авторизовался")

            self.mainwindow = MainWindow(user_id, self)
            self.mainwindow.show()
        else:
            self.statusbar.showMessage("[!] Неверный пароль или имя пользователя", 5000)

    def reg(self):
        if self.db.does_exists_user_with_this_username(self.login_le.text()):
            self.statusbar.showMessage("[!] Пользователь с таким именем уже существует", 5000)
        else:
            if login_small_validation(self.login_le.text()) and password_small_validation(self.pwd_le.text()):
                self.db.add_user(self.login_le.text(), self.pwd_le.text(), self.remember_btn.isChecked())
                self.statusbar.showMessage('[0] Пользователем с именем "{}"'
                                           ' успешно зарегистрирован'.format(self.login_le.text()), 5000)

                self.logger.log(f"Пользователь с именем {self.login_le.text()} успешно зарегистрирован")

            else:
                self.statusbar.showMessage("[!] Длина пароля должна быть больше 6, а логина - больше 3")
