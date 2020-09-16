string = "abcdefghijklmnopqrstuvwxy"


def missing_alphabets(s):
    a = "abcdefghijklmnopqrstuvwxyz"
    arr = []
    result = ""

    for i in a:
        arr.append(s.count(i))
    sets = max(arr)

    for i in range(len(arr)):
        while arr[i] < sets:
            result += a[i]
            arr[i] += 1
    return result


print(missing_alphabets(string))
