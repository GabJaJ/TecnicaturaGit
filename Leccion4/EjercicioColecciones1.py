#Ejercicio 1: Eliminar duplicados de una lista
#Escriba un programa donde tenga una lista y que a continuacion
#elimine los elementos repetidos, por último mostrar la lista.

#Creamos una lista

lista = [1, 3, 5, 'Gabriel', 5, 2,'Gabriel', 8, 34, 43, 72, 4, 9, 2, 2, 6, 1, 8, 2]
#conjunto = set(lista) #Convertimos la lista en un conjunto tipo set
#lista = list(conjunto) # Converitmos el conjunto en una lista
lista = list(set(lista)) # elimina duplicados en una sola linea de codigo

duplicates = lista.count(2)

print(lista)

print("\nLongitud de la lista:", len(lista))

print(duplicates)
#print(conjunto)







