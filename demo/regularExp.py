import re

str_temp = "China is a great country"

# findall() 函数返回包含所有匹配项的列表,如果未找到匹配，则返回空列表。
x = re.findall("a", str_temp)
print(x)
x = re.findall("U", str_temp)
print(x)

# search() 函数搜索字符串中的匹配项，如果存在匹配则返回 Match 对象, 如果未找到匹配，则返回值None
x = re.search("a", str_temp)
print("The first white-space character is located in position:", x.start())
print(x.span())  # 返回的元组包含了匹配的开始和结束位置
print(x.string)  # 返回传入函数的字符串
print(x.group())  # 返回匹配的字符串部分

# split() 函数返回一个列表，其中字符串在每次匹配时被拆分, 指定 maxsplit 参数来控制出现次数
x = re.split("\\s", str_temp)
for i in x:
    print(i)

x = re.split("\\s", str_temp, maxsplit=1)
for i in x:
    print(i)

# sub() 函数把匹配替换为您选择的文本, count 参数来控制替换次数
x = re.sub("\\s", "|", str_temp, 2)
print(x)
