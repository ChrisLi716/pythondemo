class Person:
    # 每次使用类创建新对象时，都会自动调用 __init__() 函数
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # self 参数是对类的当前实例的引用，用于访问属于该类的变量。
    def descself(self):
        return "desc myself " + self.name + "," + str(self.age) + "," + self.gender

    # 如果您不想向该类添加任何其他属性或方法，请使用 pass 关键字


class Student(Person):
    def __init__(self, name, gender, age, student_code):
        self.student_code = student_code
        # Person.__init__(self, name, gender, age)
        # super() 函数，它会使子类从其父继承所有方法和属性
        super().__init__(name, gender, age)


# 如果您在子类中添加一个与父类中的函数同名的方法，则将覆盖父方法的继承。
def descself(self):
    return Person.descself(self) + "," + self.student_code


p1 = Person("Chris", "Male", 32)
print(p1.name, p1.gender, p1.age)
print(p1.descself())

p1.age = 25
print(p1.descself())

student = Student("Ethan", "Male", 3, "00123456")
print(student.descself())
print(student.name, student.gender, student.age, student.student_code)
