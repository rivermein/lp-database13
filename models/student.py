class Student():
    def __init__(self, id=None, first_name=None, last_name=None, year_level=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.year_level = year_level

    def __str__(self) -> str:
        return str(self.id ) + ": " + self.first_name + " " + self.last_name + " (year " + str(self.year_level) + ")"
    
    
