from tables import studenttable
from tables import teachertable
from tables import subjecttable
from tables import studentsubjecttable
import csv

import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

studentIdMap = {}

with open('data/students.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    studenttable = studenttable.StudentTable()
    count = 0
    for row in reader:
        if count != 0:
            # ID,first_name,last_name,Year Level
            studentIdMap[row[0]] = studenttable.add(c=c, first_name=row[1], last_name=row[2], year_level=row[3])
        count += 1

teachersIdMap = {}

with open('data/teachers.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    teachertable = teachertable.teacherTable()
    count = 0
    for row in reader:
        if count != 0:
            teachersIdMap[row[0]] = teachertable.add(c=c, first_name=row[1], last_name=row[2])
        count += 1

subjectIdMap = {}

with open('data/subjects.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    subjecttable = subjecttable.SubjectTable()
    count = 0
    for row in reader:
        if count != 0:
            # ID,Name,Year Level,Teacher ID
            teacherId = teachersIdMap[row[3]]
            subjectIdMap[row[0]] = subjecttable.add(c=c, name=row[1], year_level=row[2], teacherid=teacherId)
        count += 1

with open('data/studentandsubject.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    studentsubjecttable = studentsubjecttable.StudentSubjectTable()
    count = 0
    for row in reader:
        if count != 0:
            # StudentID,ClassID
            studentId = studentIdMap[row[0]]
            subjectId = subjectIdMap[row[1]]
            studentsubjecttable.add(c=c, student_id=studentId, subject_id=subjectId)
        count += 1

connect.commit()
connect.close()
