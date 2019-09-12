# -*- coding: utf-8 -*-

a = 14;
b = 15;

def swap(a,b):
    temp = a
    a = b
    b = temp

#swap(a,b)
a,b = b,a

print(a)
print(b)
