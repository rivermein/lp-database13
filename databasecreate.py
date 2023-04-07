import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Student (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
firstName TEXT NOT NULL,
lastName TEXT NOT NULL,
yearLevel INTEGER NOT NULL);""")

c.execute("""CREATE TABLE IF NOT EXISTS Subject (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
yearLevel INTEGER NOT NULL,
teacherId INTEGER,
FOREIGN KEY (teacherId) REFERENCES Teacher(id));""")

c.execute("""CREATE TABLE IF NOT EXISTS Teacher (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
firstName TEXT NOT NULL,
lastName TEXT NOT NULL);""")

c.execute("""DROP TABLE IF EXISTS StudentSubject;""")

c.execute("""CREATE TABLE IF NOT EXISTS StudentSubject (studentId INTEGER NOT NULL,
subjectId INTEGER NOT NULL,
PRIMARY KEY (studentId, subjectId),
FOREIGN KEY (studentId) REFERENCES Student(id),
FOREIGN KEY (subjectId) REFERENCES Subject(id));""")

connect.commit()
connect.close()

connect = sqlite3.connect("Database.db")
c = connect.cursor()

connect.commit()
connect.close()
