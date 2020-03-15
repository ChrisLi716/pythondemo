global_v = "this is a global variable"


def func1():
    print(global_v)


def func2():
    global_v = "func2 variable"
    print(global_v)


def func3():
    global x
    x = 'this a inner variable'
    print(x)


def func4():
    global global_v
    global_v = "changed in func4"
    print(global_v)


def myname(name):
    if name != "":
        print("my name is ", name)
    else:
        print("pls input valid name")


# 默认参数值 如果我们调用了不带参数的函数，则使用默认值
def countryname(country="china"):
    print("I'm from ", country)


def add(i, j):
    return i + j


# 关键字参数
def my_kids(kid1, kid2, kid3):
    print(kid3, "is my youngest kid.")


'''任意参数
如果您不知道将传递给您的函数多少个参数，请在函数定义的参数名称前添加 *。
这样，函数将接收一个参数元组，并可以相应地访问各项：'''


def my_function(*kids):
    print("The youngest child is " + kids[2])


def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


func1()
func2()
func3()
print(x)

func4()
print(global_v)

print(myname(""))
print(countryname("US"))
print(countryname())
print(countryname(""))
print(add(7, 9))
print(my_kids(kid2="amy", kid1="hedy", kid3="ethan"))
print(my_function("Phoebe", "Jennifer", "Rory"))
print(tri_recursion(10))

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))


def myfunc(n):
    print("n=", n)
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
