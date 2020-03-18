def _99multiple():
    for i in range(1, 10):
        print_each_line(i)
        print()


def print_each_line(i):
    for j in range(1, i + 1):
        print(str(j) + "x" + str(i) + "=", i * j, end=" ")


_99multiple()
_99multiple()
