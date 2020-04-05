def listcomp():
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
    print(codes)
    codes = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(codes)


if __name__ == '__main__':
    listcomp()
