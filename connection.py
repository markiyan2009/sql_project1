import sqlite3
class Connect():
    def __init__(self):
        self.conn = sqlite3.connect("db.db")
        self.create_table()
    def create_table(self):
        cur = self.conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS connect(id_student INTEGER, id_course INTEGER)")
        self.conn.commit() 
        cur.close()      
    def add_conn(self,id_student,id_course):
        cur = self.conn.cursor()
        cur.execute("INSERT INTO connect(id_student,id_course) VALUES(?,?)",(id_student,id_course))
        self.conn.commit()
        cur.close()
    def show_connection_by_course(self,id_course):
        cur = self.conn.cursor()
        cur.execute("SELECT id_student FROM connect WHERE id_course ==?",(id_course,))
        res = cur.fetchall()
        cur.close()
        return res
