str_list = ["abc", "abc abc"]


def name_value(my_list):
    a = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for i in range(len(my_list)):
        ind = 0
        for j in range(len(my_list[i])):
            for x in range(len(a)):
                if my_list[i][j] == a[x]:
                    ind = ind + x + 1
                    break
        ind = ind * (i + 1)
        result.append(ind)
    return result


print(name_value(str_list))
