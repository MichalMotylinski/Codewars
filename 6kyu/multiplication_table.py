num = 3


def multiplication_table(size):
    arr = []
    n = size
    for i in range(size) :
        arr.append(list(range(i + 1, n + 1, i + 1)))
        n += size
    return arr


print(multiplication_table(num))
