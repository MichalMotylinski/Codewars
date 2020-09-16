data = ["abracadabra", "allottee", "assessee"]


def dup(arry):
    result = []
    for i in arry:
        current = ""
        for j in i:
            if current[-1:] == j:
                continue
            current += j
        result.append(current)
    return result


print(dup(data))
