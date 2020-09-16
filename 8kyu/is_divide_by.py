nums = [45, 5, 15]


def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False


print(is_divide_by(nums[0], nums[1], nums[2]))
