import math

def polysum(n, s):
    #calculates area
    area = (0.25*n*s*s) / math.tan(math.pi/n)
    #calculates permiter
    perimeter = s * n
    #calculates total
    total = area + perimeter* perimeter
    #returns rounded answer
    return round(total,4)