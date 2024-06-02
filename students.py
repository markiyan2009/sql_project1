import sqlite3
class Student():
    def __init__(self):

        self.conn = sqlite3.connect("db.db")
        self.create_table()
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, age INT, major TEXT)")
        self.conn.commit()
        cur.close()
    def add_student(self,name,age,major):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO students(name,age,major) VALUES(?,?,?)",(name,age,major))
        self.conn.commit()
        cur.close()
    def get_students(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM students")
        res = cur.fetchall()
        cur.close()
        return res
    def get_users_by_id(self,id_students):
        cur = self.conn.cursor()
        for id_student in id_students:
            cur.execute("SELECT name, age, major FROM students WHERE id_student == ?",(id_student,))
            print(cur.fetchone())

    def delete_user(self, id):
        cur = self.conn.cursor()
        cur.execute("DELETE FROM students WHERE nid == ?",(id))
        self.conn.commit()
        cur.close()

