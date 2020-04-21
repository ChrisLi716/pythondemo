from datetime import datetime

x = datetime.now()
print(x)
print(x.year)
print(x.strftime("%Y%m%d%H%M%S%f"))

d = datetime(2020, 5, 17)
print(d)
