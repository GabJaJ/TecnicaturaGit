
#clase dia miercoles 16/8 - primera clase 2° cuatrimestre
#laboratorio 2, python

#lista = Noelia, Nadia, Facundo, Ana, Juani, Ernesto, Bruno, Gabriel, Carlos
perricornios = ["Noelia", "Nadia", "Facundo", "Ana", "Juani", "Ernesto", "Gabriel", "Carlos"]

#Para mostrar por indices
print(perricornios[0])
print(perricornios[1])
print(perricornios[2])
print(perricornios[3])
print(perricornios[4])
print(perricornios[5])
print(perricornios[6])
print(perricornios[7])

#Para recorrer de atras hacia adelante
print(perricornios[-1])
print(perricornios[-2])
print(perricornios[-3])
print(perricornios[-4])

#recuperar rango de la lista
print(perricornios[0:2]) #solo muestra el 0 y 1
print(perricornios[:2])
print(perricornios[1:])

#modificamos un valor
perricornios[1]= "Braian"
perricornios[0]= "Carlos"
print(perricornios)

for nombres in perricornios:
    print(nombres)
else:
    print("No hay mas nombres")

#preguntamos cuantos elementos tiene
print(len(perricornios))

#agregamos un elemento
perricornios.append("Marcelo")
print(perricornios)

#insertar en un índice específico
perricornios.insert(1, "Alberto") #ingresar el indice y despues el elemento
print(perricornios) #se desplazan los demas elementos una posición al ingresar uno nuevo

perricornios.insert(3,"Debora")
print(perricornios)

#eliminamos un elemento de la lista
perricornios.remove("Alberto") #pasamos el string con el valor
print(perricornios) #muestra la lista sin el elemento seleccionado

#eliminar el ultimo elemento
perricornios.pop()
print(perricornios) #elimina el ultimo elemento de la lista, en este caso "Marcelo"

#eliminar indice específico
del perricornios[2]
print(perricornios) #desaparece el elemento de la posición 2, en este caso "Debora"

#eliminar, borrar o limpiar todos los elementos
perricornios.clear()
print(perricornios) #la lista está vacía, vemos dos []

#eliminar la lista
del perricornios # del, viene de "delete"
#print(perricornios) #tira error, lista no definida.. fue borrada

#TUPLAS
#lo escribimos entre ()
#definimos una tupla
cocina = ("cuchara", "cuchillo", "tenedor")
print(cocina)

#para ver el largo de la tupla
print(len(cocina))

#para acceder a un elemento usamos [], no ()
print(cocina[0]) #vemos el indice 0 de la tupla

#mostrar de manera inversa
print(cocina[-1]) #muestra el último elemento de la tupla, "tenedor"
print(cocina[-2]) #muestra el anteúltimo, en este caso "cuchillo"

#Accedemos a un rango
print(cocina[0:1]) #muestra ('cuchara',) --> asi se ven las tuplas, lo reconozco por la coma
print(cocina[0:2]) #muestra ('cuchara', 'cuchillo',)
#ejemplo
verduras = ('papa') #esto NO es tupla. es tipo string
print(verduras)
verduras = ('papa',) #"ahora SI es una tupla"
print(verduras)

#recorremos los elementos de la tupla
for utensillos in cocina: #print usa \n para los saltos de linea
    print(utensillos, end=' ') #finalizamos los saltos de linea y los mostramos al lado con un ' '

#cocina[0]= "plato"
#print(cocina) --> da ERROR, las tuplas no se pueden reasignar

#modificar las tuplas
#no son buena practica, solo sar cuando sea necesario
#hacemos conversion de tupla a lista
#y luego convertimos de lista a tupla

cocinaLista = list(cocina)
cocinaLista[0]= "plato" #hacemos la modificación
cocina = tuple(cocinaLista) #volvemos a convertir a tupla
print('\n',cocina) #ahora lo vemos y con el '\n' hacemos elsalto de línea

del cocina #eliminamos la tupla
#print(cocina) #cocina ya no está definido