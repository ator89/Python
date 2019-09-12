def a(x, y, z):
   if x:
      return y
   else:
      return z


def b(q, r):
   return a(q > r, q, r)

#1
print(a(False, 2, 3))

#2
print(b(3, 2))

#3
print(a(3>2, a, b))

#4
#print(b(a, b))
