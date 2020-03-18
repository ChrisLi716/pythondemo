filepath = "C:/Users/Dell/Desktop/demo.txt"
filepath2 = "C:/Users/Dell/Desktop/tmp/demo2.txt"
try:
    f = open(filepath, "a")
    f.write("hello python!")

    f = open(filepath, "r")
    print(f.read())

    f = open(filepath, "w")
    f.write("a new contents!")

    f = open(filepath, "r")
    print(f.read())

    '''
    "x" - 创建 - 将创建一个文件，如果文件存在则返回错误
    "a" - 追加 - 如果指定的文件不存在，将创建一个文件
    "w" - 写入 - 如果指定的文件不存在，将创建一个文件
    '''
    f = open(filepath2, "x")
    f = open(filepath2, "w")

finally:
    f.close()
