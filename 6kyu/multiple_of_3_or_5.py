num = 10


def solution(number):
    s = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            s = s + i
    return s


print(solution(num))
