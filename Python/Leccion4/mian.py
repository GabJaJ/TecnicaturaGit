#clase dia miercoles 16/8 - primera clase 2° cuatrimestre
#laboratorio 2, python

# Colecciones en Python

# Listas = en otros lenguajes se conocen como arreglos o vectores
# Pueden contener diferentese tipos de datos

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

for nombre in perricornios:
    print(nombre)
else:
    print("No hay mas nombre")

#preguntamos cuantos elementos tiene
print(len(perricornios))

#agregamos un elemento
perricornios.append("Marcelo")
perricornios.append([1, 2, 3])
perricornios.append(True)
perricornios.append(10)
perricornios.append([4, 5])
perricornios.append(7)
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

#TUPLAS  : Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas. Las tuplas utilizan paréntesis,
# mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.

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

#del cocina #eliminamos la tupla
#print(cocina) #cocina ya no está definido




#Tipos Set : no mantiene ningun indice, el orden es aleatorio, no permite almacenar elementos duplicados, si se puede agregar o eliminar

planetas = {'Marte', 'Júpiter', 'Venus'}
print(len(planetas))  # len = lenght

# Revisar si un elemento existe dentro de un set
print('Júpiter' in planetas)

# Agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

# Eliminar elementos, puede arrojar un error si el elementono existe
planetas.remove('Júpiter') #Esta funcion da error al ingresar un elemento erroneo o inexistente
print(planetas)
planetas.discard('tierra') # Esta fnuncion no da error aunque el objeto sea erroneo o inexistente
print(planetas)


# Limpiar set
planetas.clear()
print(planetas)

# Eliminar set o conjunto

#del planetas
#print(planetas)


# DICCIONARIO : UNA LLAVE Y UN VALOR

# coleccion de datos organizados, es otro tipo de estructura de datos de Python. No es una secuencia
# (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.
# Para explicar lo que es un diccionario en Python, es importante comprender de manera literal lo que es un diccionario.
# Un diccionario en Python funciona de la misma manera que un diccionario bilingüe. Por ejemplo, se tiene la palabra
# en español "gato" y se necesita su equivalente en francés. Lo que se haría es buscar en el diccionario para encontrar la palabra "gato".
# Eventualmente la encontrarás, y sabrás que la palabra equivalente en francés es "chat".
#
#
# En el mundo de Python, la palabra que se esta buscando se denomina clave(key). La palabra que se obtiene del
# diccionario es denominada valor.
# Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:
# 	•	Cada clave debe de ser única. No es posible tener una clave duplicada.
# 	•	Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante),
# 	o incluso una cadena.
# 	•	Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario
# 	almacena pares de valores.
# 	•	La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
# 	•	Un diccionario es una herramienta de un solo sentido. Si fuese un diccionario español-francés, podríamos buscar en español
# 	para encontrar su contraparte en francés más no viceversa.


#dict = {'key':'value', 'key':'value'}

diccionario = {
    'IDE':'Integrated Development Enviroment',
    'POO':'Programacion Orientada a Objetos',
    'SABD':'Sistema de Administracion de Base de Datos'
}

#Verificar la cantidad d e elementos del diccionartio
print(len(diccionario))
print(diccionario)

#Acceder al diccionario con la llave key

print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificamos los elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos : muestra las llaves - key
for termino in diccionario:
    print(termino)

# apra ver y recorrer el valor se necesita una funcion

for termino, valor in diccionario.items():
    print(termino, valor)

# otras maneras de acceder a un diccionario

for termino in diccionario.keys():
    print(termino) # muestra solo las llaves - key

for valor in diccionario.values():
    print(valor) # muestra los valores - value

# Comprobar la existencia de algun lemento
print('IDE' in diccionario) # devuelve un buleano
print('IDE' not in diccionario)

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)


# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar el diccionario
del diccionario


# Concatenacion de listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9]) # funcion para agregar varios elementos a la lista
print(lista3)

print(lista3.index(5)) # para saber en que indice esta el elemento indicado
# print(lista3.index(0)) daria un error por se un elemento no ingresado en la lista

# Cuantos valores hay repetidos en la lista

print(lista3.count(1))

# Para poner nuestra lista descendente o ascendente

lista3.reverse()
print(lista3)

# Para que una lista de duplique

lista = [1, 2, 3] * 2
print(lista)

lista = [lista3] * 2
print(lista3)

# Metodos de odenamietno (funcion SORT) ordena de forma ascendente
lista3.sort()
print(lista3)

lista3.sort(reverse=True) # de forma descendente
print(lista3)


# Repaso TUPLAS
# son listas inmutables y pueden tener valores diferentes - cadenas, flotantes, etc..

tupla = (4, 'Hola', 6.78, [1, 2, 3, 78], 4, 4, 'Hola')
print(tupla)


# index, count, len,
#

print(4 in tupla) # devuelve Boolean

print(5 not in tupla) # si no esta en la lista

#

#Repaso de SET o CONJUNTO
# para definir un conjunto - elementos desordenados, no puede haber duplicados solo valores unicos
# pueden tener diferentes tipos de datos

conjunto2 = set()# se puede agregar elementos
conjunto1 = {} #ya a sido incializado por lo tanto no se le puede agregar ningun dato
conjunto1={'bye', }# si ya tiene un elemento se le pueden agregar mas
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1) # preguntamos si el numero 3 no esta en el conjunto1 (booleano= verdader , no esta el numero 3 en el conjunto1


#como hacer la igualdad de dos conjuntos

print(conjunto1 == conjunto2) # nos devuelve como respuesta un booleano.

# operaciones en conjuntos
#union de conjuntos

conjunto3 = conjunto2 | conjunto1 # la linea une los conjuntos
print(conjunto3)


conjunto3 = conjunto1 & conjunto2 # que lementos tienen en comun y se van a guardar en el conjunto3
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # visualizar los lementos en el conjunto 2 y no en el conjunto1
print(conjunto3)
conjunto3 = conjunto2 - conjunto1# elementos que si estan en el conjunto 3
print(conjunto3)

#simetrica

conjunto3 = conjunto1 ^ conjunto2 # lementos no compartidos o que son diferentes entre ambos
print(conjunto3)


# como determinar si un conjunto es subconjunto de otro

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) # preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

# como saber si ambos conjuntos son disconexos que no compraten ningun dato

print(conjunto3.issuperset(conjunto1)) # preguntamos si los elementos del conjunto1 estan dentro del conjunto3
print(conjunto3.issuperset(conjunto2)) # si es verdadero quiere decir que el conjunto3 es un super conjunto
print(conjunto2.issuperset(conjunto3))


# como saber si ambos conjuntos son disconexos
# no compraten ningun elemento en comun

print(conjunto1.isdisjoint(conjunto2))


# los conjuntos no son inmutables ni totalmente mutalbes,

#convertir un conjunto totalemtne inmutable

conjunto1 = frozenset  # hace que el conjunto sea inmutable
# no se pueden agregar, modificar ni eliminar elementos del conjunto1


#Repaso DICCIONARIOS

diccionarioNuevo = {'Azul':'Blue', 'Rojo':'Red', 'Verde':'Green', 'Amarillo': 'Yellow', 'Marron': 'Brown'}
print(diccionarioNuevo)

#como eliminar

del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden contener diferentes tipòs de datos
#Agregar un diccionario dentro de otro diccionario

diccionario2 = {'Gabriel':{'Edad': 37, 'Altura': 1.85}, 'Ariel':{40, 1.83}, 'Osvaldo':{45, 1.85}, 'Natalia':{35, 1.67}}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
    11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
    24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
    19: {'Nombre': 'Nicolás Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'},
    16: {'Nombre': 'Lisandro Martinez', 'Edad': 24, 'Altura': 1.73, 'Precio': '57,37 Millones', 'Posicion': 'Defensa Centroampista'},
    7: {'Nombre': 'Rodrigo de Paul', 'Edad': 28, 'Altura': 1.80, 'Precio': '3,5 Millones', 'Posicion': 'Centrocampista'},
    14: {'Nombre': 'Exequiel Palacios', 'Edad': 23, 'Altura': 1.77, 'Precio': '24.1 Millones', 'Posicion': 'Mediocampista'},
    22: {'Nombre': 'Lautaro Martinez', 'Edad': 25, 'Altura': 1.74, 'Precio': '27 Millones', 'Posicion': 'Delantero Centro'},
    20: {'Nombre': 'Giovani Lo Celso', 'Edad': 26, 'Altura': 1.70, 'Precio': '55 Millones', 'Posicion': 'Centrocampista'},
    8: {'Nombre': 'Marcos Acuña', 'Edad': 30, 'Altura': 1.72, 'Precio': '15 Millones', 'Posicion': 'Lateral Izquierdo'}
}
print(seleccionArgentina[10])
print(seleccionArgentina)

for llave in seleccionArgentina:
    print(llave)

for llave in seleccionArgentina.values():
    print(valor)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

#como tarea agregar por lo menos 4 jugadores al diccionario seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de: ', end='')
print(len(seleccionArgentina))
print('Jugadores de la Seleccion Argentina')

# PILAS usando listas

pila = [1, 2, 3]

# se trabaja siempre con el ultimo elemento
#como agregamos elementos a la pila por el final

pila.append(4)
pila.append(5)
print(pila)

# sacar elementos por el final
elementoBorrado = pila.pop() # elimina el ultimo elemento de la lista , este se puede guardar
print(f'La pila ahora quedo asi: {pila}')
print(f'sacamos el lemento: {elementoBorrado}')



# Colas con Listas
# Estructuras de datos de tipo fifo (first input / fist output)

cola = ['Bruno', 'Nadia', 'Juan', 'Facundo']


# agregamos elementos al final de la cola

cola.append('Noelia')
cola.append('Ernesto')
print(cola)

print(f'Clientes formando fila: {cola}')
# sacamos elemto de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(f'Continuan: {cola}')

for llave, valor in seleccionArgentina.items():
    print(llave, valor)


