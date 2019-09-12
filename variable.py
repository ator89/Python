#!usr/bin/env python
# -*- coding: utf-8 -*-
# Aplicación de Hola mundo

x = "Hola mundo"
y = 10;
print(x + str(y))

print ""
print "Después ", y

while y != 0:
    print "Número actual", y
    y -= 1 


print "----------\n"

mi_lista = ['Uno','Dps','Tre','Cuatro']

for nombre in mi_lista:
    print nombre


print "\n"

for nombre in range(100,109):
    print "Informe", nombre
