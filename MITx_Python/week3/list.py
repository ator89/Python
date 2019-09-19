l = [2,4,5]

l.append(3)

l2 = [7,9,1]

l3 = l + l2

#sort without mutate
print(sorted(l3))

#delete by index
del(l2[1])

print(l2)

#pop
l3.pop()

#remove key
l3.remove(9)
print(l3)


s = 'hola'

print(list(s))

nombre = 'angel'
nombre.split('g')
print(nombre.split('g'))

print('__'.join(s))

#mutates
#l.reverse()
#l.sort()