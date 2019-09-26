def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        #print('no aqui')
        return 0
    elif x < a:
        print('no aqui tampoco')
        return x
    else:
        print('no aqui')
        return rem(x-a, a)

print(rem(7, 5))