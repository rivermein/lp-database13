from models.teacher import Teacher
from models.subject import Subject


class teacherTable:
    def add(self, c, first_name, last_name):
        c.execute(
            "INSERT INTO Teacher (firstName, lastName) VALUES (" +
            "'" + first_name + "', '" + last_name + "');"
        )
        teacher_id = c.execute("SELECT id FROM Teacher ORDER BY id DESC LIMIT 1;").fetchone()[0]
        return teacher_id

    def get_by_id(self, c, query):
        c.execute(
            "SELECT id, firstName, lastName FROM Teacher WHERE id = '" + str(query) + "';"
        )
        teacher = None
        for row in c.fetchall():
            teacher = Teacher()
            teacher.id = row[0]
            teacher.first_name = row[1]
            teacher.last_name = row[2]
        return teacher

    def get_all(self, c):
        c.execute("SELECT * FROM Teacher")
        teacher = None
        teachers = []
        for row in c.fetchall():
            teacher = Teacher()
            teacher.id = row[0]
            teacher.first_name = row[1]
            teacher.last_name = row[2]
            teachers.append(teacher)
        return teachers

    def get_subjects(self, c, teacher_id):
            c.execute(
                "SELECT * FROM Subject WHERE teacherId =" + str(
                    teacher_id) + ";")
            subjects = []
            for row in c.fetchall():
                subject = Subject()
                subject.id = row[0]
                subject.name = row[1]
                subject.year_level = row[2]
                subject.teacher_id = row[3]
                subjects.append(subject)
            return subjects

    def update(self, c, teacher):
        c.execute(
            "UPDATE Teacher SET firstName = '" + teacher.first_name + "', lastName = '" + teacher.last_name + "' WHERE id =" + str(teacher.id) + ";"
        )

    def delete(self, c, teacher):
        c.execute(
            "DELETE FROM Teacher WHERE id =" + str(teacher.id) + ";"
        )

    def delete_by_id(self, c, teacher_id):
        c.execute(
            "DELETE FROM Teacher WHERE id =" + str(teacher_id) + ";"
        )
