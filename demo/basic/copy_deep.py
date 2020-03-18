#!/usr/bin/python
# -*-coding:utf-8 -*-
import copy

a = {"a": [1, 2, 3], 2: [1, 2, 3]}
# shallow copy
b = a.copy()
print("a", a, "b", b)

a["a"].append(5)
print("a", a, "b", b)

# deep copy
b = copy.deepcopy(a)
a[2].append(6)
print("a", a, "b", b)
