
class User():
    def __init__(self, db):
        self.table_name = 'Users'
        self.db = db

    def find_all(self):
        retVal = []
        con = self.db.get_connection()
        cur = con.cursor(buffered=True)
        cur.execute("SELECT * FROM %s LIMIT 15 OFFSET 0"%(self.table_name))
        rows = cur.fetchall()
        for row in rows:
            ob = {}
            for i, col in enumerate(cur.description):
                ob[col[0]] = row[i]
            retVal.append(ob)
        con.close()
        return retVal

    def find_by_username_password(self, username, password):
        con = self.db.get_connection()
        cur = con.cursor()
        cur.execute("""SELECT username, password 
                       FROM Users 
                       WHERE username='{0}' AND password='{1}'
                    """.format(username, password))
        row = cur.fetchone()
        cur.close()
        con.close()
        return row



