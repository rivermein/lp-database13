from tables import studenttable
import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

test = studenttable.StudentTable()

student_id = test.add(c=c, first_name="Fred", last_name="Boots", year_level="9")
connect.commit()
print(student_id)

student = test.get_by_id(c, student_id)
print("student = " + str(student))

print(*test.get_all(c))

student.year_level = 10
test.update(c, student)
connect.commit()
students = test.get_by_year_level(c, 10)
print("student = " + str(students[len(students)-1]))
student.first_name = "Mince"
test.update(c, student)
student_got = test.get_by_name(c, "fred")
try:
    print("student = " + str(student_got[len(student_got)-1]))
except:
    print("there is no student with that name.")
    student_got = test.get_by_name(c, "Mince")
try:
    print("student = " + str(student_got[len(student_got)-1]))
except:
    print("there is no student with that name.")

test.delete(c, student)
connect.commit()
student = test.get_by_id(c, student_id)
print(str(student is None))

connect.close()
