"""
如果有某种内容，则几乎所有值都将评估为 True。
除空字符串外，任何字符串均为 True。
除 0 外，任何数字均为 True。
除空列表外，任何列表、元组、集合和字典均为 True
"""

# bool() 函数可让您评估任何值，并为您返回 True 或 False
x = 0
y = 10
print(bool(x))
print(bool(y))

'''实际上，除空值（例如 ()、[]、{}、""、数字 0 和值 None）外，没有多少值会被评估为 False。当然，值 False 的计算结果为 False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

#  isinstance() 函数，该函数可用于确定对象是否具有某种数据类型
a = 'my name is chris'
print(isinstance(a, str))
