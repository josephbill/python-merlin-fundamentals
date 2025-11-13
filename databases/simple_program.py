import sqlite3

DB_NAME = 'school.db'

def connect_db():
    return sqlite3.connect(DB_NAME)

def add_student(name,age,grade):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO students (name,age,grade) VALUES (?,?,?)', (name,age,grade))
    conn.commit()
    conn.close()
    
def read_student():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students')
    data = cur.fetchall()
    conn.close()
    return data 

## extend this script to cover basis on update and deleting of records : create those functions 

# example usage 
name = input("Enter Student Name : ")
age = int(input("Enter Student Age : "))
grade = input("Enter Student Grade : ")

add_student(name,age,grade)
print(read_student())