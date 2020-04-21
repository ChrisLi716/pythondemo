"""desc the class proprieties"""


class Clz:
    name = "clz"
    clz_date = "2020-03-15"
    __age = None

    def __init__(self, name, date):
        self.name = name
        self.clz_date = date
        self.__age = 12

    def desc_clz_instance(self):
        print(self.name, self.clz_date)

    # 类方法中不能访问类实例的属性，如果需要访问则需要用类名或_class_
    # 定义类方法时不需要self参数,classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
    # 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    @classmethod
    def desc_clz(cls):
        print(cls.name, cls.clz_date)
        print(Clz.name, Clz.clz_date)
        if cls.__age is None:
            print("__age is None")
            Clz("Chris", "2020-03-20")
            print(Clz.__class__.__age)

    @classmethod
    def desc_clz_proprieties(cls):
        print("__name__:", cls.__name__)
        print("__doc__:", cls.__doc__)
        print("__module__:", cls.__module__)
        print("__bases__:", cls.__bases__)
        print("__dict__:", cls.__dict__)


c = Clz("Chris", "2020-03-20")
# c.desc_clz_instance()
# c.desc_clz()
c.desc_clz_proprieties()
