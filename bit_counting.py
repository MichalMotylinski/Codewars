num = 1234


def count_bits(n):
    bit = "{0:b}".format(n)
    s = 0
    for i in str(bit):
        if i == "1":
            s = s + 1
    return s


print(count_bits(num))
