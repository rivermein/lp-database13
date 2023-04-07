from tables import teachertable
import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

test = teachertable.teacherTable()

teacher_id = test.add(c=c, first_name="Oliver", last_name="Green")
connect.commit()
print(teacher_id)

teacher = test.get_by_id(c, teacher_id)
print("teacher = " + str(teacher))

teacher.first_name = "Boris"
test.update(c, teacher)
connect.commit()
teachers = test.get_by_id(c, teacher_id)
print("teacher = " + str(teachers))

test.delete(c, teacher)
connect.commit()
teacher = test.get_by_id(c, teacher_id)
print(str(teacher is None))

connect.close()
