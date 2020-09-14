nums = [10, 35, 14, 9, 39, 23, 35]


def stem_and_leaf(data):
    x = 0
    y = 10
    result = {}
    while x < 10:
        leafs = []
        for i in data:
            if y > i >= y - 10:
                if i < 10:
                    leafs.append(int(str(i)[0]))
                else:
                    leafs.append(int(str(i)[1]))
        if leafs:
            leafs.sort()
            result[x] = leafs
        x += 1
        y += 10
    return result


print(stem_and_leaf(nums))
