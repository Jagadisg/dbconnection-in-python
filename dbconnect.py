import mysql.connector

class dbcon:
    def __init__(self):
        global con
        global cur
        pass

    def connect(self,dbhost = "localhost",dbuser = "root", dbpass="" , dbname = ""):
        self.con = mysql.connector.connect(host = dbhost, user = dbuser , passwd = dbpass, database=dbname)
        self.cur = self.con.cursor()

    def __del__(self):
        self.con.close()
    
    def getsql(self, sql = ""):
        if(sql == "" ): 
            print("Query is Null")
            return ""
        
        try:
            self.cur.execute(sql)
            result = self.cur.fetchall() 
            return result
        except:
            print("SQL ERROR")
            return ""
    
    def setsql(self, sql = ""):
        if(sql == "" ): 
            print("Query is Null")
            return False
        
        try:
            self.cur.execute(sql)
            self.con.commit()
            return True
        except:
            print("SQL ERROR")
            return False
        
    def showtable(self, tablename):
        return self.getsql(f"SELECT * FROM {tablename}")

