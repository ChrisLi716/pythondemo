import People


class Student(People):
    def __init__(self, name, gender, age, student_code):
        self.student_code = student_code
        People.__init__(self, name, gender, age)

    def descself(self):
        return People.descself(self) + "," + self.student_code


s1 = Student("Ethan", "Male", 3, "00123456")
print(s1.descself())
