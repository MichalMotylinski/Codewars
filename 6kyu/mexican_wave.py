string = "hello a"


def wave(people):
    arr = []
    for i in range(len(people)):
        if people[i] == " ":
            continue
        s = people[:i + 1].upper() + people[i + 1:]
        s = people[:i].lower() + s[i:]
        arr.append(s)
    return arr


print(wave(string))
