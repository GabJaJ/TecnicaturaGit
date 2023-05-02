from Persona2 import Persona2 # importamos la CLASE, se puede oimportar mas de una CLASE, con el "+" se importa todo.

print('Creacion de objetos' .center(50, '_'))

if __name__ == '__main__' : # comprobacion del metodo principal en ejecucion, de esta manera cuando se importen nuevos tipos desde otros modulos el codigo de prueba no se va a ejecutar
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles() # nos muestra todos los objetos que tenemos en persona2

    print(__name__)

# Destructor de objetos

print('Eliminacion de Objetos' .center(50, '-')) # genera una cadena centrada a traves de establecer la cantidad de caractreres y un caracter para usar

# ELIMINAMOS el objeto persona5, no es muy visto
del persona5
