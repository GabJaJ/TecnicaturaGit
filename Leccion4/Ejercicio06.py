# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por Ejemplo:
# Si digita el 5 la lista tendra: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

numero = int(input('Digite un número: '))
lista = [] # creamos una lista vacía
for i in range(1, 11):
    lista.append(i*numero) #llenamos la lista multiplicando el iterador que va recorriendo por la variable  numero


print(f'\nTabla de multiplicar del {numero}: \n {lista}')

for indice, i in enumerate(lista):
    print(f'{i} x {numero} = {lista[indice]}')
