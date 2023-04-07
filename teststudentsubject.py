from tables import studentsubjecttable
from tables import studenttable
from tables import subjecttable
import sqlite3

connect = sqlite3.connect("Database.db")
c = connect.cursor()

# need to create student and subject to test this
teststudent = studenttable.StudentTable()
student_id = teststudent.add(c=c, first_name="Fred", last_name="Boots", year_level="9")
connect.commit()

testsubject = subjecttable.SubjectTable()
subject_id = testsubject.add(c=c, name="Maths", year_level="9", teacherid=None)
other_subject_id = testsubject.add(c=c, name="P.E", year_level="9", teacherid=None)
connect.commit()


try:
    test = studentsubjecttable.StudentSubjectTable()

    print("records = " + str(test.count_all(c)))

    student_id_and_subject_id = test.add(c=c, student_id=student_id, subject_id=subject_id)
    connect.commit()
    print(student_id_and_subject_id)
    print("records after add = " + str(test.count_all(c)))

    studentsubject = test.get_by_id(c, student_id, subject_id)
    print("studentsubject = " + str(studentsubject))


    test.delete_by_id(c, other_subject_id, student_id)
    #test.delete(c, studentsubject)
    connect.commit()
    studentsubject = test.get_by_id(c, student_id, other_subject_id)
    print(str(studentsubject is None))

    print("records = " + str(test.count_all(c)))
finally:
    teststudent.delete_by_id(c, student_id)
    testsubject.delete_by_id(c, subject_id)
    testsubject.delete_by_id(c, other_subject_id)

connect.close()
