class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("{}, {}".format(self.name, self.roll))

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks
