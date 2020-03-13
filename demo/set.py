# set 集合是无序和无索引,不重复的集合，不可以修改里面的元素但是可以增加里面的元素

set1 = {1, 3, 4, 5}
print(set1)
# print(set1[2])
for x in set1:
    print(x)

x = 8
print(x in set1)

# 集合一旦创建，您就无法更改项目，但是您可以添加新项目
set1.add("apple")
print(set1)
set2 = {"orange", "banana", "cherry"}
set1.update(set2)
print(set1)

set1.remove("banana")
print(set1)

# 如果要删除的项目不存在，则 remove() 将引发错误
# set1.remove("www")
# print(set1)

set1.discard("apple")
print(set1)

set1.discard("www")
print(set1)

set3 = {"a", "b", "c"}
set4 = set1.union(set3)
print(set4)

print(set4.pop())
print(set4.clear())
