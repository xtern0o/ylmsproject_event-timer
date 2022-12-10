import datetime as dt


class Logger:
    def __init__(self):
        self.fname = "source/logs/logs.txt"

    def log(self, text):
        with open(self.fname, mode="a", encoding="utf-8") as f:
            current_datetime_str = dt.datetime.today().strftime("%Y.%m.%d %H:%M:%S")
            f.write(f"[{current_datetime_str}]: {text}\n")

    def clear_logs(self):
        with open(self.fname, mode="w", encoding="utf-8") as f:
            f.write('')
