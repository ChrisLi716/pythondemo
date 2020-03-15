# i = 0
# while i < 7:
#     print(i)
#     i += 1

j = 0
while j <= 10:
    if j % 2 == 0:
        print("j=", j)
        break
    j += 1

m = 0
while m <= 10:
    if m % 2 == 0:
        m += 1
        continue
    print("m=", m)
    m += 1
else:
    print("m is not less than 10")

# range() 函数返回一个数字序列，默认情况下从 0 开始，并递增 1（默认地），并以指定的数字结束。
for x in range(10):
    print(x)

# 通过添加参数来指定起始值
for x in range(3, 10):
    print(x)

# 通过添加第三个参数来指定增量值
for x in range(3, 50, 10):
    print("step=10", x)
else:
    print("out of scope")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
