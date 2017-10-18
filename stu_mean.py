import sqlite3
import csv

f = "discobandit.db"

db = sqlite3.connect(f)
c = db.cursor()

#======

def create_avg_table():
    c.execute("CREATE TABLE peeps_avg (student TEXT PRIMARY KEY, id INTEGER, avg REAL)")
    list_of_students = look_up_students()
    id = 1
    while (id < len(list_of_students)):
        command = "INSERT INTO peeps_avg VALUES('%s', %d, %d)" % (list_of_students[id-1], id, compute_avg(id))
        c.execute(command)
        id+=1

def look_up_students(): # creates a list of students to be iterated through
    c.execute("SELECT name FROM peeps")
    students = c.fetchall()
    list_of_students = []
    for student in students:
        list_of_students.append(student[0])
    return list_of_students

def look_up_grades(id_number): # looks up student's grades based on their id
    c.execute("SELECT mark FROM courses WHERE id = " + str(id_number))
    # print 'ID #' + str(id_number)
    marks = c.fetchall()
    list_of_marks = []
    for mark in marks:
        list_of_marks.append(mark[0])
    return list_of_marks # returns a list of the student's grades
    
def compute_avg(id_number): # determines the average of the student
    mark_total = 0 # adds up all of a student's marks
    number_of_marks = 0 # counts how many marks a student has
    list_of_marks = look_up_grades(id_number)
    for mark in list_of_marks:
        mark_total+=mark
        number_of_marks+=1
    return float(mark_total) / number_of_marks

def display_grades():
    c.execute("SELECT * FROM peeps_avg")

def update_avg(id_number):
    command = "UPDATE peeps_avg SET avg = %d WHERE id = %d" % (compute_avg(id_number), id_number)

def add_course(code, mark, id):
    command = "INSERT INTO courses VALUES('%s', %d, %d)" % (code, mark, id)
    c.execute(command)

    
c.execute("DROP TABLE peeps_avg")
create_avg_table()
display_grades()

#======

db.commit()
db.close()
