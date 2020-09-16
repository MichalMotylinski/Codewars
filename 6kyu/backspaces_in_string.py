string = "abc#d##c"


def clean_string(s):
    for i in s:
        if i == "#":
            if s.index(i) - 1 >= 0:
                s = s[:s.index(i) - 1] + s[s.index(i):]
            s = s.replace("#", "", 1)
    return s


print(clean_string(string))
