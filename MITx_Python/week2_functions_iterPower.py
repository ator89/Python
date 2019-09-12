def iterPower(x, exp):

    if exp == 0:
        return 1
    total = 1
    i = 0
    while i < exp:
        total = x * total
        i += 1
    return total

print(iterPower(2,4))

