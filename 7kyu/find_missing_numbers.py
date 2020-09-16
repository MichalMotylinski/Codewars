array = [-3, -2, 1, 5]


def find_missing_numbers(arr):
    missed = []
    if len(arr) > 0:
        for x in range(arr[0], arr[-1]):
            if x not in arr:
                missed.append(x)
    return missed


print(find_missing_numbers(array))
