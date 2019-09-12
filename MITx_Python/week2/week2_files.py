import math

def polysum(n, s):
    area = (0.25*n*s*s) / math.tan(math.pi/n)
    perimeter = s * n

    total = area + perimeter* perimeter
    return round(total,4)

print(polysum(64,15))

#994879.6834
