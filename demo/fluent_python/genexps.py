colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ((c, s) for c in colors for s in sizes):
    print(tshirt)

# 元组其实是对数据的记录：元组中的每个元素都存放了记录中一个字段的数据，外加这个
# 字段的位置。正是这个位置信息给数据赋予了意义。
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
# 元组里的元素，也叫作拆包（unpacking），因为元组中第二个元素对我们没有什么用，所以它赋值给“ _ ”占位符
for country, _ in traveler_ids:
    print(country)
