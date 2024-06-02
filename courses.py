import sqlite3
class Course():
    def __init__(self):
        self.conn = sqlite3.connect("db.db")
        self.create_table()
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS courses(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, instuction TEXT)")
        self.conn.commit()
        cur.close()
    def add_course(self,name,instuction):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO courses(name,instuction) VALUES(?,?)",(name,instuction))
        self.conn.commit()
        cur.close()
    def get_courses(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM courses")
        res = cur.fetchall()
        cur.close()
        return res
    def delete_course(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM courses WHERE id = ?",(id,))
        self.conn.commit()
        cur.close()

