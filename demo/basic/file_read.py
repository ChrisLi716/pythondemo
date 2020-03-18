try:
    f = open("C:/Users/Dell/Desktop/demo.txt")
    # print(f.read(5))
    # print(f.read())
    # print(f.readline())
    for x in f:
        print(x, end='')
finally:
    f.close()
