s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])

l = list(range(10))
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100
l[2:5] = [100]
print(l)