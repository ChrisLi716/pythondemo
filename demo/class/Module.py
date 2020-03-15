import platform as pl
import Person
from Module2 import greeting

x = pl.system()
print(x)

# 可以列出模块中的所有函数名（或变量名）
# x = dir(pl)
# for i in x:
#     print(i)

p = dir(Person)
for i in p:
    print(i)

print(greeting("chris"))
