tuple1 = ("apple", "banana", "cherry")
print(tuple1)

print(tuple1[1])
print(tuple1[1:3])
print(tuple1[-3:-1])

list1 = list(tuple1)
list1.append("pear")
list1.insert(2, "pipe apple")
tuple1 = tuple(list1)
print(tuple1)

tmp = "oo"
if tmp in tuple1:
    print(tmp, " is in this tuple")
else:
    print(tmp, " is not in this tuple")

# tuple1[1] = "coconut"

# 如需创建仅包含一个项目的元组，您必须在该项目后添加一个逗号，否则 Python 无法将变量识别为元组。
tuple2 = ("car",)
print(type(tuple2))

tuple3 = tuple1 + tuple2
print(tuple3)

idx = tuple3.index("cherry")
print(idx)
