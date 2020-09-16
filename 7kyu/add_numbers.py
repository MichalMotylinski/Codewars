n1 = 2
n2 = 11


def add(num1, num2):
    result = ""
    arr1 = [x for x in str(num1)][::-1]
    arr2 = [x for x in str(num2)][::-1]
    for i in range(len(arr1)):
        try:
            s = int(arr1[i]) + int(arr2[i])
        except IndexError:
            s = int(arr1[i])
        result = str(s) + result
    if len(arr2) > len(arr1):
        for i, j in enumerate(arr2, start=0):
            if i >= len(arr1):
                result = str(j) + result
    return int(result)


print(add(n1, n2))
