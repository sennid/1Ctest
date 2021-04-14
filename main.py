def finddiff(old, new):
    file = open(    'D:\\1Ctest\\diff.txt', 'wb')
    b1 = old.read(1)
    b2 = new.read(1)
    dif1 = 0
    while b1 == b2 and (b1 != '' and b2 != ''):
        b1 = old.read(1)
        b2 = new.read(1)
        dif1 += 1
    file.write(bytes(str(dif1), 'utf8'))
    dif2 = dif1
    while b1 != b2 and (b1 != '' and b2 != ''):
        b1 = old.read(1)
        b2 = new.read(1)
        dif2 += 1
    file.write(bytes(str(dif2), 'utf8'))

    file.close()
    return r"D:\\1Ctest\\diff.txt"


def recover(old, diff):
    file = open('D:\\1Ctest\\new.txt', 'wb')
    file.write(bytes('mmm', 'utf8'))
    file.close()


f1 = open('D:\\1Ctest\\11.txt', 'rb')
f2 = open('D:\\1Ctest\\22.txt', 'rb')
name = finddiff(f1, f2)
f0 = open(name, 'rb')
recover(f1, f0)
