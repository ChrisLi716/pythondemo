def print_each_line(i):
    for j in range(1, i + 1):
        print(str(i) + "x" + str(j) + "=", i * j, end=" ")


def _99multiple():
    for i in range(1, 10):
        print_each_line(i)
        print()


_99multiple()
_99multiple()
