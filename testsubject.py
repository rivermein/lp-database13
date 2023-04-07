from tables import subjecttable
import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

test = subjecttable.SubjectTable()
print("records = " + str(test.count_all(c)))

subject_id = test.add(c=c, name="Maths", year_level="9", teacherid=1)
connect.commit()
print(subject_id)

subject = test.get_by_id(c, subject_id)
print("subject = " + str(subject))

subject.year_level = 10
test.update(c, subject)
connect.commit()
subjects = test.get_by_year_level(c, 10)
print("subjects = " + str(subjects[len(subjects)-1]))
subjects = test.get_by_teacher(c, 2)
print("subjects = " + str(subjects[len(subjects)-1]))
students = test.get_students(c, 3)
print("students taking this subject: " + str(students[len(students)-1]))

test.delete(c, subject)
connect.commit()
subject = test.get_by_id(c, subject_id)
print(str(subject is None))

print("records = " + str(test.count_all(c)))

connect.close()
