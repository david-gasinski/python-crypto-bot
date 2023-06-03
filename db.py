import sqlite3

class DB():
    def __init__(self, DB):
        self.conn = sqlite3.connect(DB)
        self.cur = self.conn.cursor()

    def update_record(self, id: int, val: str):
        self.cur.execute("UPDATE users SET wallet=? WHERE id=?", (val, id))
        self.con.commit()

    def remove_record(self, id: str):
        self.cur.execute("DELETE FROM users WHERE id=?", id)

    def add_record(self, id: int, wallet: str):
        self.cur.execute("INSERT INTO users VALUES (?, ?)", (id, wallet))
        self.conn.commit()

    def get_record(self, id: int):
        return self.cur.execute("SELECT * from users WHERE id=?", id)
    