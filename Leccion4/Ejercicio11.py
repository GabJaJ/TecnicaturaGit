# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el el telefono, el programa tendra el siguiente menú de opciones
#   1. Nuevo Contacto
#   2. Borrar Contacto
#   3. Ver contactos existentes
#   4. Salir

agenda = {}
while True:
    print('\t.:MENÚ:.')
    print('1. Nuevo Contacto.')
    print('2. Borrar Contacto.')
    print('3. Ver contactos existentes.')
    print('4. Salir.')
    opcion = int(input('DIgite una opcion del menú: '))
    if opcion == 1:
        nombre = input('Digite el nombre del contacto: ')
        telefono = input('Digite el numero de telefono: ')
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('COntacto agregado exitosamente!.')
        else:
            print('Este nombre de contacto ya existe.')
    elif opcion == 2:
        nombre = input('Cuál es el nombre del contacto: ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto requerido')
        else:
            print('Este contacto no existe en la agenda.')
    elif opcion == 3:
        print('Agenda de contactos: ')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfoo: {valor}')
    elif opcion == 4:
        print('Gracias por utilizar su agenda de contactos.')
        break
    else:
        print('Se equivoco de opcion de menú.')
    print()

