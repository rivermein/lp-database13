class Subject():
    def __init__(self, id=None, name=None, year_level=None, teacher_id=None):
        self.id = id
        self.name = name
        self.teacher_id = teacher_id
        self.year_level = year_level

    def __str__(self) -> str:
        return str(self.id) + ": " + self.name + ", taught by " + str(self.teacher_id) + " (available to year " + str(self.year_level) + ")"


