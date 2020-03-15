# 要把对象/类创建为迭代器，必须为对象实现 __iter__() 和 __next__() 方法


class Mynumber:

    # 必须始终返回迭代器对象本身
    def __iter__(self):
        self.a = 1
        return self

    # 返回序列中的下一个项目
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


mynumber = Mynumber()
myiter = iter(mynumber)

# for x in myiter:
#     print(x)

for x in range(30):
    print(next(myiter))
