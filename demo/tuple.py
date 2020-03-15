# 元组是有序且不可更改的集合

tuple1 = ("apple", "banana", "cherry")
print(tuple1)

print(tuple1[1])
print(tuple1[1:3])
print(tuple1[-3:-1])

'''创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组'''
list1 = list(tuple1)
list1.append("pear")
list1.insert(2, "pipe apple")
tuple1 = tuple(list1)
print(tuple1)

print("the second of tuple1", tuple1[2])
# 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目
print(tuple1[-5:-1])

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

tuple_temp = ("apple", "banana", "cherry")
for x in tuple_temp:
    print("tuple_temp", x)
