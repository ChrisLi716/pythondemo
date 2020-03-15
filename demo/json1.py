import json

x = '{ "name":"Bill", "age":63, "city":"Seatle"}'

y = json.loads(x)
print(type(y))
print(y["age"])

x = {
    "name": "Bill",
    "age": 63,
    "city": "Seatle"
}

jsonstr = json.dumps(x)
print(repr(jsonstr))

# 当 Python 转换为 JSON 时，Python 对象会被转换为 JSON（JavaScript）等效项
# Python	JSON
# dict	    Object
# list	    Array
# tuple	    Array
# str	    String
# int	    Number
# float	    Number
# True	    true
# False	    false
# None	    null
print(json.dumps({"name": "Bill", "age": 63}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "Bill",
    "age": 63,
    "married": True,
    "divorced": False,
    "children": ("Jennifer", "Rory", "Phoebe"),
    "pets": None,
    "cars": [
        {"model": "Porsche", "mpg": 38.2},
        {"model": "BMW M5", "mpg": 26.9}
    ]
}

print(json.dumps(x))
# separators =（", ", ": "），默认值, 这意味着使用逗号和空格分隔每个对象，使用冒号和空格将键与值分开
print(json.dumps(x, indent=4))
# 使用 sort_keys 参数来指定是否应对结果进行排序
print(json.dumps(x, indent=4, sort_keys=True))
