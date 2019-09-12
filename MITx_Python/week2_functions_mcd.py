def mcd(a,b):
    div = 0
    vis = 0
    tot = 0

    if a > b:
        div = a
        vis = b
    else:
        div = b
        vis = a

    tot = div % vis

    while tot != 0:
        div = vis
        vis = tot
        tot = div % vis

    return div