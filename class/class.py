class Student:
    def __init__(self, name, year, enroled, gpa):
        self.name = name
        self.year = year
        self.enroled = enroled
        self.gpa = gpa
    def display_info(self):
        print("The student " + self.name + "'s GPA is " + str(self.gpa))
    def gratuation(self):
        if self.enroled and self.gpa > 2.5 and self.year == 12:
            print(self.name + " will be able to graduate this year")
        else:
            print(self.name + " will not be able to graduate this year")

mitsuha = Student("Mitsuha", 12, True, 1.8)
taki = Student("Taki", 12 , True, 2.6)

mitsuha.display_info()
taki.display_info()
mitsuha.gratuation()
taki.gratuation()    