listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

#listA.remove(3)
listA.insert(0,100)
listA.append(7)

print(listA+listB)

listB.sort()
listB.pop()
print(listB)

listB.remove('x')
print(listB)

listA.extend([4, 1, 6, 3, 4])

listA.reverse()
print(listA)