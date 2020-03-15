a = 10
b = 20
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")

# 如果只有一条语句要执行，则可以将其与 if 语句放在同一行
m = 50
n = 10
if m > n: print("m is greater than n")

m = 5
# 如果只有两条语句要执行，一条用于 if，另一条用于 else，则可以将它们全部放在同一行
print("m is greater than n") if m > n else print("m is not great than n")

str1 = "hello"
str2 = "world"
if str1 == "hello" and str2 == "world":
    print(str1, str2)
else:
    print("not match")

a = 200
b = 66
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

if a > b:
    pass

