# Ejercicio 7:  Juego adivina el número
# Realizar un juego para adivinar un número. Para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# números indicando 'es mayor' o 'es menor' segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el numero de intentos para lograrlo.

import  random # invocamos un numero random
print('\tBienvenido a Adivina el número!:') # Con "\t" tabulamos el texto
aleatorio = random.randint(1, 100) # cramos una variable con un numeor aleatorio entre 1 - 100.
contador = 0 # creamos una variable contador iniciada en 0
while True: # Mientras sea verdadero seguira andando
    numero = int(input('Digite un número: '))
    contador += 1 # aumenta en 1
    if numero > aleatorio:
        print('\tNo es el número, digite un número menor.')
    elif numero < aleatorio:
        print('\tNo es le número, digite un numero mayor.')
    else:
        print(f'\tFELICIATIONES, Usted a adivinado el número {aleatorio}!!')
        break # rompe el ciclo y bucle
print(f'\nNúmero de intentos: {contador}')






