# python -m pip install mysql-connector

from dbconnect import dbcon

db = dbcon()
db.connect(dbname="demodb")

for row in db.showtable('students'):
    print(row[0])


if db.setsql("INSERT INTO students(s_name,s_age,s_std,remark) VALUES('Rohan',30,'10th','std')"):
    print("Succefully inserted ")
    print(db.showtable('students'))
else:
    print("ERROR")