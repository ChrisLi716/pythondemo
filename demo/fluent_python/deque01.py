from collections import deque

#  maxlen 是一个可选参数，代表这个队列可以容纳的元素的数量，而且一旦设定，这个属性就不能修改了
dq = deque(range(10), maxlen=10)
print(dq)
# 队列的旋转操作接受一个参数 n ，当 n > 0 时，队列的最右边的 n 个元素会被移动到队列的左边。当 n < 0 时，最左边的 n 个元素会被移动到右边
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
# 当试图对一个已满（ len(d) == d.maxlen ）的队列做尾部添加操作的时候，它头部的元素会被删除掉。注意在下一行里，元素 0 被删除了
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
