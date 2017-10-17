import sqlite3
import csv

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

#======
#c.execute("CREATE TABLE averages (id INTEGER PRIMARY KEY, avg INTEGER)")

i = 1
while i < 11:
    c.execute("SELECT mark FROM courses WHERE id = " + str(i))
    print 'ID #' + str(i)
    marks = c.fetchall()
    print marks
    i+=1

#======

db.close()
