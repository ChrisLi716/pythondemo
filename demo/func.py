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


func1()
func2()
func3()
print(x)

func4()
print(global_v)
