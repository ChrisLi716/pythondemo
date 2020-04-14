list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c"]

list_emp = list1.__add__(list2)
print(list_emp)
print(list1)

list1.__iadd__(list2)
print(list1)

mylist = [1, 2, 3, 4, 5, 'a', 'b', 'c']
print(mylist[:2])
print(mylist[2:])

print(mylist[-3:-1])
