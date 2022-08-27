#Rango de 0 a 10 con numeros divisibles entre 3
0
3
6
9

x = int(input("Ingrese un valor entero: "))

"""   for c in range(0,x), incremento (2):
    if c % 3 == 0:
        continue
    print(c)
for i in range(0, 11):
    if i % 3 != 0:
        print(i)"""
for i in range(3,10,2):
    print(i)

#Rango con valores de inicio =2 y fin =6
2
3
4
5
6
x = int(input("Ingrese un valor entero: "))

for i in range(2,6):
    print(i)

#Rango con valores de inicio =3, fin =10, incremento =2
3
5
7
9

x = int(input("Ingrese un valor entero: "))

for i in range(3,10, 2):
    print(i)
    if i  == -1:
        break





#process finished with exit code 0


#Ejercicio Tupla


#Dada la siguiente Tupla
tupla = (13, 1, 8, 3, 2, 5, 8) #Definimos la Tupla
#Crear una lista que solo incluyan los numeros menores a 5
#e imprimir por consola [1, 3, 2]


for i in range(len(tupla)):
    if tupla[i] < 5:
        print(tupla[i])


