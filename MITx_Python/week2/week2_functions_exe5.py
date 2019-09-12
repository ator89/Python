def foo(x, y=5):
    def bar(x):
        return x + 1

    return bar(y * 2)


print(foo(3))


def foo2(x, y=5):
    def bar(x):
        return x + 1

    return bar(y * 2)


print(foo(3, 0))

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

print(foo(2))

def foo4 (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

print(foo4(5))