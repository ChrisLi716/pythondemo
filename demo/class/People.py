class People:
    # 每次使用类创建新对象时，都会自动调用 __init__() 函数
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    # self 参数是对类的当前实例的引用，用于访问属于该类的变量。
    def descself(self):
        return "desc myself " + self.name + "," + str(self.age) + "," + self.gender
