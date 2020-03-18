# python 中的字符串字面量由单引号或双引号括起。
c = 'hello world'
d = "hello world"
if c.__eq__(d):
    print(True)
else:
    print(False)

if c == d:
    print(True)
else:
    print(False)

str = """Python is a widely used general-purpose, high level programming language. 
It was initially designed by Guido van Rossum in 1991 
and developed by Python Software Foundation. 
It was mainly developed for emphasis on code readability, 
and its syntax allows programmers to express concepts in fewer lines of code."""

print(str)

str1 = 'hello, world!'
print(str1[2])
# 获取从位置 2 到位置 5（不包括）的字符
print(str1[2:5])
# 获取从位置 5 到位置 1 的字符，从字符串末尾开始计数：
print(str1[-5:-2])

print(str1[0: len(str1)])

# strip() 方法删除开头和结尾的空白字符：
c = "  CHRIS LI  "
print(c.strip())

# lower() 返回小写的字符串：
print(c.lower().strip())
# upper() 方法返回大写的字符串：
d = "hello chris christoph"
print(d.upper())

# replace() 用另一段字符串来替换字符串：
print(d.replace("chr", "hedy"))

# split() 方法在找到分隔符的实例时将字符串拆分为子字符串
print(d.split(","))

# 如需检查字符串中是否存在特定短语或字符，我们可以使用 in 或 not in 关键字
print("" in d)

striter = iter(d)
print(next(striter))

print(d.capitalize())
