import sqlite3


class Db:
    """Класс, специализированный для работы с бд events.db"""
    def __init__(self):
        self.con = sqlite3.connect("source/database/events.db", check_same_thread=False)
        self.cur = self.con.cursor()

    def get_userid_if_correct_pwd(self, login: str, password: str) -> int:
        """Returns user_id if pwd is correct else return 0"""

        data = self.cur.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (login, )).fetchone()
        if data:
            if password == str(data[2]):
                return data[0]  # user id
            else:
                return 0

    def find_remembered_user(self) -> tuple:
        """Finds user who is remembered and returns boolean value"""

        data = self.cur.execute("""
        SELECT * FROM users
        WHERE remember = 1
        """).fetchone()
        return data

    def set_remembered(self, user_id: int, remembered: bool) -> None:
        """Changes the value of remember"""

        self.cur.execute("""
        UPDATE users
        SET remember = ?
        WHERE id = ?
        """, (remembered, user_id))
        self.con.commit()

    def does_exists_user_with_this_username(self, username: str) -> bool:
        """If exists user with this username returns True"""

        return self.cur.execute("""SELECT * FROM users WHERE username = ?""", (username, )).fetchone() is not None

    def get_user_data(self, user_id: int) -> tuple:
        """Gets user data tuple, where
        data[0] - user id
        data[1] - user name
        data[2] - password
        data[3] - remember"""

        return self.cur.execute("""
            SELECT * FROM users
            WHERE id = ?
        """, (user_id, )).fetchone()

    def get_events_from_this_user(self, user_id: int) -> list:
        """Returns all the events created by this user"""

        data = self.cur.execute("""
        SELECT * FROM events
        WHERE owner_id = ?
        """, (user_id, )).fetchall()
        return data

    def add_user(self, username: str, pwd: str, remember: bool) -> None:
        """Register new user"""

        self.cur.execute("""
        INSERT INTO users(username, password, remember)
        VALUES (?, ?, ?)
        """, (username, pwd, remember))
        self.con.commit()

    def add_event(self, name: str, date: str, color: str, owner_id: int) -> None:
        """Add new event to the data base"""

        self.cur.execute("""
        INSERT INTO events (name, date, color, owner_id)
        VALUES (?, ?, ?, ?)
        """, (name, date, color, owner_id))
        self.con.commit()

    def delete_event(self, id: int) -> None:
        """Deletes event with this id"""

        self.cur.execute("""
        DELETE FROM events
        WHERE id = ?
        """, (id, ))
        self.con.commit()

    def update_event_properties(self, id: int, new_name: str, new_color: str) -> None:
        """Updates name and color of event with this id"""

        self.cur.execute("""
        UPDATE events
        SET name = ?, color = ?
        WHERE id = ?
        """, (new_name, new_color, id))
        self.con.commit()
