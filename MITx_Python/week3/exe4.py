aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList

print(bList)

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:
        dList.append(num)
cList == dList

print(cList)

cList[2] = 20
print(cList)
print(dList)