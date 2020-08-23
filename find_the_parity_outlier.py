arr = [2, 4, 0, 100, 4, 11, 2602, 36]


def find_outlier(integers):
    even_counter = 0
    odds_counter = 0
    even_num = 0
    odd_num = 0
    for i in integers:
        if (i % 2) == 0:
            even_counter += 1
            if even_counter == 1:
                even_num = i
        else:
            odds_counter += 1
            if odds_counter == 1:
                odd_num = i

        if even_counter > 1 and odds_counter == 1:
            return odd_num

        elif odds_counter > 1 and even_counter == 1:
            return even_num


print(find_outlier(arr))
