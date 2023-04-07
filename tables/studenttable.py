from models.student import Student
from models.subject import Subject


class StudentTable:

    def add(self, c, first_name, last_name, year_level):
        """adds a student and returns their new id"""
        c.execute(
            "INSERT INTO Student (firstName, lastName, yearLevel) VALUES (" +
            "'" + first_name + "', '" + last_name + "', '" + year_level + "');"
        )
        student_id = c.execute("SELECT id FROM Student ORDER BY id DESC LIMIT 1;").fetchone()[0]
        return student_id

    def get_all(self, c):
        c.execute("SELECT * FROM Student ORDER BY lastName, firstName")
        student = None
        students = []
        for row in c.fetchall():
            student = Student()
            student.id = row[0]
            student.first_name = row[1]
            student.last_name = row[2]
            student.year_level = row[3]
            students.append(student)
        return students

    def get_by_id(self, c, query):
        c.execute(
            "SELECT id, firstName, lastName, yearLevel FROM Student WHERE id = '" + str(query) + "';"
        )
        student = None
        for row in c.fetchall():
            student = Student()
            student.id = row[0]
            student.first_name = row[1]
            student.last_name = row[2]
            student.year_level = row[3]
        return student

    def get_by_year_level(self, c, query):
        c.execute(
            "SELECT id, firstName, lastName, yearLevel FROM Student WHERE yearLevel = " + str(query) + ";"
        )
        students = []
        for row in c.fetchall():
            student = Student()
            student.id = row[0]
            student.first_name = row[1]
            student.last_name = row[2]
            student.year_level = row[3]
            students.append(student)
        return students

    def get_by_name(self, c, query):
        c.execute(
            "SELECT id, firstName, lastName, yearLevel FROM Student WHERE firstName LIKE '%" + query + "%' OR lastName LIKE '%" + query + "%';"
        )
        students = []
        for row in c.fetchall():
            student = Student()
            student.id = row[0]
            student.first_name = row[1]
            student.last_name = row[2]
            student.year_level = row[3]
            students.append(student)
        return students

    def get_subjects(self, c, student_id):
        c.execute("SELECT s.* FROM Subject s JOIN studentsubject ss ON ss.subjectId = s.id WHERE ss.studentId =" + str(student_id) + ";")
        subjects = []
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
            subjects.append(subject)
        return subjects

    def update(self, c, student):
        c.execute(
            "UPDATE Student SET firstName = '" + student.first_name + "', lastName = '" + student.last_name + "', yearLevel = "
            + str(student.year_level) + " WHERE id =" + str(student.id) + ";"
        )

    def delete(self, c, student):
        c.execute(
            "DELETE FROM Student WHERE id = " + str(student.id) + ";"
        )

    def delete_by_id(self, c, student_id):
        c.execute(
            "DELETE FROM Student WHERE id = " + str(student_id) + ";"
        )
