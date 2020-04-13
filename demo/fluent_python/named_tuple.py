from collections import namedtuple, OrderedDict

'''
创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可
以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串。
'''
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

print(tokyo.country)
print(tokyo.population)
print(tokyo[0])

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)

print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ':', value)
