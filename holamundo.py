# -*- coding: utf-8 -*-
#from __future__ import 

class Persona:
    usuario = ""
    __password = ""

    def __init__(self, user):
        self.usuario = user

    def setPassword(self, passw):
        self__password = passw
    def getPassword(self):
        return self.__password
    def mostrarDatos(self):
        print("Usuario: ", self.usuario)
        print("Contrasna: ", self.getContrasenia())

def menu():
    opcion = input("Seleccione una opción: ")
    
done = False

def registrar():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")

while not done:
    opcion = input("""\tMenu\n1 - Opción 1\n2 - Opcion 2\n3 - Opción 3\n0 - Salir""")
    if( opcion == 1):
        print("opcion 1")
        done = True

    if( opcion == 2):
        print("opcion 2")
        done = True

done = True

