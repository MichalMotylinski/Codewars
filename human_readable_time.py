import math

integer = 5


def make_readable(seconds):
    h = math.floor(seconds / 3600)
    m = math.floor(seconds / 60) - (h * 60)
    s = seconds % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)


print(make_readable(integer))
