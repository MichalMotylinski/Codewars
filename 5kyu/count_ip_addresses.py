address1 = "10.0.0.0"
address2 = "10.0.0.50"


def ips_between(start, end):
    arr1 = [x for x in start.split(".")][::-1]
    arr2 = [x for x in end.split(".")][::-1]
    i = 0
    multiplier = 1
    total = 0
    while i < len(arr2):
        total += ((int(arr2[i]) - int(arr1[i])) * multiplier)
        i += 1
        multiplier *= 256
    return total


print(ips_between(address1, address2))
