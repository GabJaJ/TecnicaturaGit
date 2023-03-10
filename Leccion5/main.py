# Comenzamos con Funciones
# mi funcion() # No se puede llamar antes de definir una funcion
# Definimos una funciona
def mi_funcion(): # Para identificar a la funciona utilizamos parentesis
     print('Saludos a todos los aliumnos de Tecnicatura')

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name + ' ' + lastName)
person = ['Ariel', 'Betancud']
show(person[0], person[1]) # Pasamos unopor uno los datos de la lista a lafuncion
show(*person) # Esto es lo mismo que lo anterior pero lo pasamos todo junto
person2 = ('Osvaldo', 'Giordanini') # desempaquetamos a traves de una tupla
show(*person2)
person3 = {'lastName': 'Lucero', 'name': 'Natalia'}
show(**person3)

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break  # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se terminó')

# List comprehension, lista de comprensión
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe'] #Lista de Strings
alongP= [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista con una condicion
print(alongP)

bottleC = [{'name': 'Quilmes', 'Country': 'Arg'},
           {'name': 'Corona', 'Country': 'Mx'},
           {'name': 'Stella Artois', 'Country': 'Belgium'},
           ] #Creamos un diccionario
Arg = [b for b in bottleC if b['Country'] == 'Arg'] # Creamos un diccionario para guardar lo que necesitamos de otro diccionario,
# recoriendo en singular elemento por elemento del diccionario bottleC con una condicion si el elemento es igual al varo de Arg en string entonces se va a crear el diccionario Arg
print(bottleC)
print(Arg)

# Paso de Argumentos (funciones)
def mi_funcion2(name, lastName):
    print('Saludos a todos los que ven a traves del canal de YouTube')
    print(f'Nombre: {name}, Apellido: {lastName}')
mi_funcion2('Jorge', 'Lucero')
mi_funcion2('Ariel', 'Betancud')
mi_funcion2('Analia', 'Pedrosa')

# La palabra return en funciones
# Creamos una función para sumar
def sumar(a, b):
    return a + b
resultado = sumar(78, 22)
# print('El resultado de la suma es : {resultado')
print(f'El resultado de la suma es: {sumar(55, 45)}') # ejecutamos la función desde la misma función print

def sumar2(a: int = 0, b: int = 0) -> int: # Le damos un valor por default
    return a + b
resultado2 = sumar2()
print(f'Resultado de la suma: {resultado2}')
print(f'Resultado de la suma: {sumar2(22, 66)}')

# Argumentos, variables en funciones
def listaNombres(*nombres): # no sabemos cuantos datos van a ingresar, NOrmalmente se utiliza : *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listaNombres('Lucas', 'José', 'Claudia', 'Rosa', 'Maria')
listaNombres('Marcos', 'Daniel', 'Romina', 'Pepe', 'Marcela', 'Carlos')

def listarTerminos(**terminos) # Lo mas ultilizado es **kwargs para recibir los argumentos, lsita de elementos Tupla
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos() · No recibe nada, nada se va a mostrar
listarTerminos(IDE='Integrated Development Enviroment', PK='Primary Key')
listarTerminos(Nombre='Leonel Messi') # no se puede utilizar un valor numerico

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito', 'Pedro', 'Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10, 11) # No es objeto iterable
desplegarNombres((10, 11)) #Ahora si se puede iterar al transformarlo en una Tupla, si es solo un dato no olvidar la ultima coma
desplegarNombres([22, 55]) # Ahora se genero una lista

# Funciones Recursivas (se ejecurtara hasta que logre su objetivo)
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero + factorial(numero-1) # Caso recursivo

resultado = factorial(5)
print(f'El factorial del numero 5 es: {resultado}')

#Tarea: que el usuario ingrese el numero para calcular el factorial












