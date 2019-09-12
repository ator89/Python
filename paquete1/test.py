# -*- coding: utf-8 -*-

menu = True
opcion = -1

def menu():
    print("\tMENU\n")
    print("1 - Login")
    print("2 - Registro")
    print("0 - Salir") 

while(menu): 
    menu()
    #opcion = raw_input("Seleccion una opcion: ")
    opcion = input()
    while(opcion != 0):
      menu()
      # opcion = raw_input("Seleccione una opcion: ")
      # print("Hola")
      
