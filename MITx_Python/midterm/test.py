import operator
from functools import reduce



x = "pi"
y = "pie"

x,y = y,x
print(y)

def f(x ,j):
    while x >= 0:
        while j >= 0:
            print(x, j)

#print(f(5,6))


def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(-4))

def count2(n):
    count = 0
    cadena = str(n)

    for i in range(len(cadena)):
        if cadena[i] == '7':
            count += 1
    return count

def countNums(n):
    t = str(n)
    if t == '1':
        return 1
    else:
        return 1 + countNums(t[:-1])

def count7(n):
    n = str(n)
    if not n:
        return 0
    if n.startswith('7'):
        return 1 + count7(n[1:])
    else:
        return count7(n[1:])

print(count7(17277747))


L = [[1,2], [2,3], [5,6,7]]

def deep_reverse(L):
    L2 = []
    for i in range(len(L)):
        L[i].reverse()
        L2.append(L[i])
    L2.reverse()
    L[:] = L2

deep_reverse(L)
print(L)


adict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

def uniqueValues(aDict):
    countMap = {}
    for val in aDict.values():
        countMap[val] = countMap.get(val, 0) + 1
    uni = [k for k, v in aDict.items() if countMap[v] == 1]
    return uni

print(uniqueValues(adict))


ll = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(alist):
    if alist == []:
        return []
    elif type(alist) is not list:
        return [alist]
    else:
        return flatten(alist[0]) + flatten(alist[1:])



print(flatten(ll))


def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    i = 0
    while len(L) > i:
        if f(L[i]):
            i += 1
        else:
            L.pop(i)
    return len(L)

L = ['a', 'b', 'a', 'e']


