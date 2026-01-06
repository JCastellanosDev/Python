class Student:
    def __init__(self, name, year, enroled, gpa):
        self.name = name
        self.year = year
        self.enroled = enroled
        self.gpa = gpa
    def display_info(self):
        print("The student " + self.name + "'s GPA is" + str(self.gpa))

mitsuha = Student("Mitsuha", "Sophomore", True, 3.8)
taki = Student("Taki", "Junior", True, 3.6)

mitsuha.display_info()
taki.display_info()
    