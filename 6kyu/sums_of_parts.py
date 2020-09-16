ls = [0, 1, 3, 6, 10]
i = 0
list1 = []

sum1 = sum(ls)
list1.append(sum1)

for i in ls:
    sum1 = list1[-1] - i
    list1.append(sum1)

print(list1)
