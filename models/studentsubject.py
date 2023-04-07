class StudentSubject:
    def __init__(self, student_id=None, subject_id=None):
        self.student_id = student_id
        self.subject_id = subject_id

    def __str__(self) -> str:
        return "Student " + str(self.student_id) + " is in class " + str(self.subject_id)
