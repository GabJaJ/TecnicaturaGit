# Dada la siguiente tupla
import math

tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e importar por consola [1, 3, 2]

lista = [] # Definimos la lista
# Filtramos los elementos menores a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

# Ejercicio de matematicas
# PAra sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error -> Debería ser un número positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\nSu raíz cuadrada es: {math.sqrt(numero):.2f}') # ".2f denota la cantidad de decimales habra en el resultado de la raiz cuadrada



