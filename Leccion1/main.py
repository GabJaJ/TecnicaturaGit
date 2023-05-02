"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos!!"
print(miVariable)
miVariable = 3.5
print(miVariable)
miVariable = "Chau a todos!!"
print(miVariable)
x = 10
y = 2
z = x + y
print(z)
print(id(x))
print(id(y))
print(id(z))
# las literales se escriben x352, y096

#Tipos int, float, String, Bool

x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de Cadenas (Strings)

miGrupoFavorito = "The Mars Volta "
caracteristicas = "Great Progressive Rock Band!"
print("Mi Grupo Favorito es: " + miGrupoFavorito + "" + caracteristicas)
#el simbolo "+" sirve para concatenar y no como operacion

#otra forma de imprimir Strings
print("Mi Grupo Favorito es: ", miGrupoFavorito, caracteristicas)


numero1 = "7" #hardcode - codigo duro - ya se le asigna un valor
numero2 = "9"
print(numero1 + numero2) # se concatenan
print(int(numero1) + int(numero2))

#Tipo booleano (bool)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print("El Resultado es verdadero")
else:
    print("El Resultado es falso")


#Procesar los datos ingresados por el usuario
#Funcion input - regresa dato tipo String
#resultado = input("Digite un numero: ")
#print(resultado)

#Conversion de la entrada de datos
#Funcion Input
numero12 = int(input("Ingrese el primer digito: "))
numero23 = int(input("Ingrese el segundo digito: "))
resultado = numero12 + numero23
print("El resultado de la suma es: ", resultado)



edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print("Es mayor de edad: ", edad)
else:
    print("Es menor de edad", edad)


a = int(input("Digite un numero: "))
print(f"El residuo de la division es: {a % 2}")
if a % 2 == 0:
     print(f"El valor de a es: {a} es numero PAR")
else:
     print(f"El valor de a es: {a} es un numero IMPAR")


edadAdulto = 18
edadPersona = int(input("Digite su edad: "))
if edadPersona >= edadAdulto:
     print(f"Su edad es: {edadPersona} años, usted es mayor de edad.")
else:
     print(f"Su edad es: {edadPersona} años, usted es menor de edad.")


Ejercicio el Mayor de dos numero


"""















