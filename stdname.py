
#from dbconnect import dbcon
import dbconnect as dbc

# db = dbcon()
db = dbc.dbcon()
db.connect(dbname="demodb")
