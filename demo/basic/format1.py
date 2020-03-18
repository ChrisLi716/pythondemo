price = 52
txt = "The price is {:.2f} dollars"
print(txt.format(price))

# 索引号
quantity = 3
itemno = 567
price = 52
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 63
name = "Bill"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# 命名索引
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Porsche", model="911"))

# 通过字典设置参数需要解包
school_desc = "my school is {school_name}, the page is {url}, the prinple is{prinple}"
school_dict = {"school_name": "YALE", "url": "www.yale.com", "prinple": "Chris"}
print(school_desc.format(**school_dict))
