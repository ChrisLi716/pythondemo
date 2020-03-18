# 字典是一个无序、可变和有索引的集合

dict1 = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
print(dict1)

print(dict1["year"])
print(dict1.get("model"))

for x in dict1:
    print(x, dict1.get(x))

for x in dict1.values():
    print(x)

for x, y in dict1.items():
    print(x, y)

if "model" in dict1:
    print("Yes, 'model' is one of the keys in the dict1 dictionary")

# 打印字典中的项目数
print(len(dict1))

dict1["color"] = "red"
print(dict1)

# pop() 方法删除具有指定键名的项
v = dict1.pop("brand")
print("pop the specified key", v)
print(dict1)

# 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）
v = dict1.popitem()
print(v)
print(dict1)

del dict1["year"]
print(dict1)

dict1.clear()
print("clear", dict1)

# del dict1
# print("del", dict1)

dict2 = dict1.copy()
dict1["name"] = "chris"
print(dict1)
print(dict2)

dict3 = dict(dict1)
dict1["address"] = "sz cn"
print(dict1)
print(dict3)

myfamily = {
    "child1": {
        "name": "Phoebe Adele",
        "year": 2002
    },
    "child2": {
        "name": "Jennifer Katharine",
        "year": 1996
    },
    "child3": {
        "name": "Rory John",
        "year": 1999
    }
}

for x in myfamily.values():
    for m, n in x.items():
        print(m, n)

for x, y in myfamily.items():
    for m, n in y.items():
        print(x, m, n)
