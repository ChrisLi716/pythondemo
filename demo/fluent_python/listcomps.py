def listcomp():
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
    print(codes)

    codes = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(codes)

    for x in symbols:
        if ord(x) > 127:
            print(x, ord(x))


if __name__ == '__main__':
    listcomp()
