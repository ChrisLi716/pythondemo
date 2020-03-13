# 字典是一个无序、可变和有索引的集合

dict1 = {
    "brand": "Porsche",
    "model": "911",
    "year": 1963
}
print(dict1)

print(dict1["year"])
print(dict1.get("model"))

for x in dict1:
    print(x, dict1.get(x))

for x in dict1.values():
    print(x)

for x, y in dict1.items():
    print(x, y)

if "model" in dict1:
    print("Yes, 'model' is one of the keys in the dict1 dictionary")

dict1.pop("model")