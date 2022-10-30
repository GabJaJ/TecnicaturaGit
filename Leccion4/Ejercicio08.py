# Ejercicio 8: Menú interactivo - Cajero automatico
# Hacer un programa que simule un cajero automatico con un saldo
# inicial de $1000 y tendrá el siguiente menú de opciones
#                 1.- Ingresar dinero a la cuenta
#                 2.- Retirar dinero de la cuenta
#                 3.- Mostrar dinero disponible
#                 4.- Salir

saldo = 1000
while True:
    print('\t.:MENÚ:.')
    print('1.- Ingresar dinero a la cuenta:.')
    print('2.- Retirar dinero de la cuenta.')
    print('3.- Mostrar dinero disponible.')
    print('4.- Salir.')
    opcion = int(input('Digite una opción de menú: '))
    print() #salto de linea
    if opcion == 1:
        extra = float(input('Cuanto dinero desea ingresar -> ')) #se guardara el monto ingresado con decimales en la variable extra
        saldo += extra # suma el extra al saldo
        print(f'Dinero en la cuenta: ${saldo}')
    elif opcion == 2:
        retirar = float(input('Cuanto dinero desea retirar -> '))
        if retirar > saldo:
            print('No tiene saldo suficiente, intente.')
        else: # si el retiro no es mayor al saldo continua el retiro
            saldo -= retirar # se resta el valor que se retira al saldo
            print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 3:
        print(f'Dinero en la cuenta al momento: ${saldo}')
    elif opcion == 4:
        print('Gracias por utilizar su cajero automatico, hasta pronto.')
        break
    else: # en caso de que no seleccione un opcion existente
        print('Se equivoco de opcion de menú.')
        print()







