#import tests.Sum as t01
#from tests.Sum import Suma
from tests import Sum

result = Sum.Suma(1,3)
print(result)

x = "hola mundo"
print(x)

respuesta = int(input("Ingrese una opción: "))

if respuesta == 1:
    print("Ingresaste uno")
elif respuesta == 2:
    print("Ingresaste dos")
elif respuesta == 5:
    print("cinco")
else:
    print("Ingresaste otra cosa")

lista = ["uno","dos","tres"]

i = 0
while i <= 2:
    print(lista[i])
    i += 1

print("\nAdiós")
