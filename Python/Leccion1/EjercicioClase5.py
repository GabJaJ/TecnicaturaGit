"""

valor = int(input("Ingrese un valor del 1 al 5: "))
if valor>=0 and valor<=5:
    print("Mi valor es: ", valor)
else:
    print("El valor es incorrecto")



valor = int(input("Ingrese un valor: "))
if valor>=0 and valor<=20 or valor<=30:
    print("Esta denrto del rango de lo 20 - 30 :", valor)
else:
    print("Fuera de Rango")



edad= int(input("Digite su edad: "))
veinte= edad >= 20 and edad < 30
print(veinte)
treinta = edad >= 30 and edad < 40
print(treinta)

if veinte or treinta:
    if veinte:
        print("Estas dentro del Rango de los (20\'0) años.")
    elif treinta:
        print("Estas dentro del rango de los 30\'0) años.")
    else:
      print("No estas dentro del rango")
else:
   print("No estas dentro del rango de los 20 o 30.")



numero1= int(input("Digite el primer numero: "))
numero2= int(input("Digite el segundo numero: "))
NumeroMayor = numero1 >= numero2
print(numero1)
NumeroMayor2 = numero1 <= numero2
print(numero2)

if NumeroMayor or NumeroMayor2:
    if NumeroMayor:
        print("Es mayor: .", NumeroMayor)
    elif NumeroMayor2:
        print("Es mayor: .", NumeroMayor2)
    else:
      print("No es Mayor")
else:
   print("No es Mayor.")


Mostrar= int(input("Digite el primer numero: "))
Libro= int(input("Digite el segundo numero: "))
numero2= int(input("Digite el segundo numero: "))
NumeroMayor = numero1 >= numero2
print(numero1)
NumeroMayor2 = numero1 <= numero2
print(numero2)

if NumeroMayor or NumeroMayor2:
    if NumeroMayor:
        print("Es mayor: .", NumeroMayor)
    elif NumeroMayor2:
        print("Es mayor: .", NumeroMayor2)
    else:
      print("No es Mayor")
    else:
      print("No es Mayor.")


#Ejercicio: Tienda de libros!!
#1. Mostrar: Ingrese los siguientes datos del libro
#2. Digite el nombre del libro
#3. Digite el ID del libro
#4. Digite el precio del libro
#5. Indicar si el envío es gratuito (True/False)
#6.
#Mostrar:
#Nombre:
#ID:
#Precio:
#Envío Gratuito?

print("Ingrese la siguiente informacion hacerca del libro: ")
nombre = input ("Digite el nombre del Libro: ")
id = in(input("Digite el ID del Libro: "))
precio = float(input("Digite el precio del libro: "))
evioGratuito = input("Indicar si el envio es gratuito (True/False): ")
if envioGratuito == "True":
     envioGratuito = True
if envioGratuito == "False":
     envioGratuito = False
else:
     envioGratuito = "El valor es incorrecto"
print(f"""
           Nombre: {nombre}
           id: {id}
           precio: {precio}
           Envio Gratuito: {envioGratuito}
""")


















