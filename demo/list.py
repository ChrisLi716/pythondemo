'''
列表（List）是一种有序和可更改的集合。允许重复的成员.
元组（Tuple）是一种有序且不可更改的集合。允许重复的成员.
集合（Set）是一个无序和无索引的集合。没有重复的成员.
词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员.
'''

list_temp = ["apple", "banana", "cherry"]
print(list_temp)
print(list_temp[0])
# 负索引表示从末尾开始，-1 表示最后一个项目，-2 表示倒数第二个项目，依此类推
print(list_temp[-1])
print(list_temp[0:2])
print(list_temp[-3:-1])

list_temp[1] = 456
print(list_temp)

for x in list_temp:
    print(x)

print(456 in list_temp)

print("---------inner func---------")
list_temp.append("456")
print(list_temp)
list_temp.insert(2, 'hello')
print(list_temp)
list_temp.pop()
print(list_temp)
list_temp.pop(2)
print(list_temp)
list_temp.remove("apple")
print(list_temp)
del list_temp[0]
print(list_temp)
# del list_temp
# print(list_temp)
list2 = ['I', '4']
print(list2)
list2.clear()
print(list2)

list1 = ["apple", "banana", "cherry"]
list2 = list1
print(list2)
list1[0] = "pear"
print(list2)

list2 = list1.copy()
print(list2)
list1.append("pipe apple")
print(list1)
print(list2)

list3 = list1 + list2
print(list3)

list1.extend(list2)
print(list1)

x = list1.count("banana")
print(x)
# ASC
list1.sort()
print(list1)
# DESC
list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

idx = list1.index("banana")
print(idx)
