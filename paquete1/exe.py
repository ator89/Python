# -*- coding: utf-8 -*-
from __future__ import print_function

def info():
    nombre = raw_input("Nombre")
    print("Tu nombre es "+nombre)
info()

def tabla():
    T = [[4,7,8],[1,8,3,6],[5,7,0,9]]

    for i in T:
        for j in i:
            print (j, end=" ")


def funcion_uno():
    print ("Aja")

tabla()
#funcion_uno()
