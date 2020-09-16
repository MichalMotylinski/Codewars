import re
s = "TestTestTestTest"
sub = "TestTest"


def find_nth_occurrence(substring, string, occurrence=1):
    arr = []
    for i in range(len(string)):
        j = string[i:i + len(substring)]
        if substring == j:
            arr.append(i)
    if len(arr) >= occurrence:
        return arr[occurrence - 1]
    else:
        return -1


print(find_nth_occurrence(sub, s, 1))
