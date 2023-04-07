from models.studentsubject import StudentSubject


class StudentSubjectTable:
    def add(self, c, student_id, subject_id):
        c.execute(
            "INSERT INTO StudentSubject (studentId, subjectId) VALUES (" +
            "'" + str(student_id) + "', '" + str(subject_id) + "');"
        )
        return student_id, subject_id

    def get_by_id(self, c, first_query, second_query):
        c.execute(
            "SELECT studentId, subjectId FROM StudentSubject WHERE studentId = " + str(first_query) + " AND subjectId = '" + str(second_query) + "';"
        )
        studentsubject = None
        for row in c.fetchall():
            studentsubject = StudentSubject()
            studentsubject.student_id = row[0]
            studentsubject.subject_id = row[1]
        return studentsubject

    def delete(self, c, studentsubject):
        c.execute(
            "DELETE FROM StudentSubject WHERE studentId = " + str(studentsubject.student_id) + " AND subjectId =" + str(studentsubject.subject_id) + ";"
        )

    def delete_by_id(self, c, subject_id, student_id):
        c.execute(
            "DELETE FROM StudentSubject WHERE studentId = " + str(student_id) + " AND subjectId =" + str(
                subject_id) + ";"
        )

    def count_all(self, c):
        return c.execute("SELECT COUNT(*) FROM StudentSubject").fetchone()
