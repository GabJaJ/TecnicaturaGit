# Ejercicio 5: Factorial de un número positivo
# Hcer un programa para calcular el factorialde un numero positivo

numero = int(input('Digite un numero: '))
while numero < 0: # Mientras el numero sea negativo
    print('Error -> El numero tiene que ser positivo')
    numero = int(input('Digite un número: '))
factorial = 0 # la variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\nEl factorial del numero {numero} ingresado es: {factorial}')


