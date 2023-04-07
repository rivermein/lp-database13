from models.student import Student
from models.subject import Subject


class SubjectTable:
    def add(self, c, name, year_level, teacherid):
        c.execute(
            "INSERT INTO Subject (name, yearLevel, teacherId) VALUES (" +
            "'" + name + "', '" + str(year_level) + "', '" + str(teacherid) + "');"
        )
        subject_id = c.execute("SELECT id FROM Subject ORDER BY id DESC LIMIT 1;").fetchone()[0]
        return subject_id

    def get_all(self, c):
        c.execute("SELECT * FROM Subject")
        subject = None
        subjects = []
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
            subjects.append(subject)
        return subjects

    def get_by_id(self, c, query):
        c.execute(
            "SELECT id, name, yearLevel, teacherId FROM Subject WHERE id = '" + str(query) + "';"
        )
        subject = None
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
        return subject

    def get_by_year_level(self, c, query):
        c.execute(
            "SELECT id, name, yearLevel, teacherId FROM Subject WHERE yearLevel = " + str(query) + ";"
        )
        subjects = []
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
            subjects.append(subject)
        return subjects

    def get_by_teacher(self, c, teacher_id):
        c.execute(
            "SELECT id, name, yearLevel, teacherId FROM Subject WHERE teacherId = " + str(teacher_id) + ";"
        )
        subjects = []
        for row in c.fetchall():
            subject = Subject()
            subject.id = row[0]
            subject.name = row[1]
            subject.year_level = row[2]
            subject.teacher_id = row[3]
            subjects.append(subject)
        return subjects

    def update(self, c, subject):
        query = "UPDATE Subject SET name = '" + subject.name + "', yearLevel = '" + str(subject.year_level) + "', teacherId = "\
                + str(subject.teacher_id) + " WHERE id =" + str(subject.id) + ";"
        c.execute(query)

    def delete(self, c, subject):
        c.execute(
            "DELETE FROM Subject WHERE id =" + str(subject.id) + ";"
        )

    def delete_by_id(self, c, subject_id):
        c.execute(
            "DELETE FROM Subject WHERE id =" + str(subject_id) + ";"
        )

    def count_all(self, c):
        return c.execute("SELECT COUNT(*) FROM Subject").fetchone()

    def get_students(self, c, subject_id):
        c.execute("SELECT s.* FROM Student s JOIN studentsubject ss ON ss.studentId = s.id WHERE ss.subjectId =" + str(subject_id) + ";")
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
