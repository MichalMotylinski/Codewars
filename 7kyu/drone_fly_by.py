lamps = "xxxxx"
drone = "===T"


def fly_by(lamps, drone):
    i = 0
    lamps_on = ""
    while i < len(lamps):
        if i < len(drone):
            lamps_on = lamps_on + "o"
        else:
            lamps_on = lamps_on + "x"
        i += 1
    return lamps_on


def fly_by2(lamps, drone):
    i = 0
    on = ""
    while i < len(drone) and i < len(lamps):
        on = on + "o"
        i += 1
    return "".join((on, lamps[len(drone):]))


print(fly_by(lamps, drone))
