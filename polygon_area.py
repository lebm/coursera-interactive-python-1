import math


def polygon_area(sides, side_length):
    return (sides * side_length**2)/(4*math.tan(math.pi/sides))


print polygon_area(7, 3)
