import sqlite3

# connects to db / creates the db if it doesn't exist 
conn = sqlite3.connect('school.db')

# create a cursor reference : to execute our SQL commands 
cursor = conn.cursor()

# create a table for students 
cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    '''
)
# Insert - create records to our table  : INSERT INTO SQL STATEMENT 
# ? placeholder preventing direct SQL Injection : - Prepared Statements 
# cursor.execute(
#     'INSERT INTO students (name,age,grade) VALUES (?,?,?)',("Joseph",20,"8th")
# )
# cursor.execute(
#     'INSERT INTO students (name,age,grade) VALUES (?,?,?)',("Jane",20,"8th")
# )

# Update : UPDATE statement -> WHERE : -> filtering  (pick the unique field on filtering)
cursor.execute(
    'UPDATE students SET grade = ? , age = ? WHERE id = ?' , ("10th","22",2)
)

# DELETE : delete -> WHERE :
cursor.execute(
    'DELETE FROM students WHERE id = ? ', (4,)
)


# read : select return a lists , .fetchall()
cursor.execute(
    'SELECT * FROM students'
)
rows = cursor.fetchall()  # returns a list of tuples 
for row in rows:
    print(row) # tuple


conn.commit()  #saves the changes to the DB
conn.close()  # closes the connection to the DB 