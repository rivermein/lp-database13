class Teacher():
    def __init__(self, id=None, first_name=None, last_name=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return str(self.id) + ": " + self.first_name + " " + self.last_name


