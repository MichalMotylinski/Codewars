l = ["a", "b", "c"]


def number(lines):
    arr = []
    for i in range(len(lines)):
        arr.append(str(i + 1) + ": " + lines[i])
        i += 1
    return arr


print(number(l))
