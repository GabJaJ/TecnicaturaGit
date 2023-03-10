from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):  # creamos un metodo que trabaja con el objeto de las otras clases EMpleado y Gerente
    # print(objeto)  # de manera indirecta llama al str de la clase Empleado o la clase Gerente
    print(type(objeto))  # para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles()) # mostramos de la clase padre Empleado
    if isinstance(objeto, Gerente): # metodo de instancia para acceder a un objeto no detallado en la clase padre
        print(objeto.departamento) # por si solo no se peude imprimir solo lo hace al pasar por la instancia



# con el polimorfismo tenemos diferentes formas de mostrar la informacion a traves de diferentes metodos

empleado = Empleado('Mariano', 50000)  # creamos el primer objeto de la clase empleadi
imprimir_detalles(empleado)

gerente = Gerente('Romina', 65000, 'Sistemas')  # creamos un objeto de la clase hija
imprimir_detalles(gerente)

gerente2 = Gerente('Pablo', 65000, 'Caja')
imprimir_detalles(gerente2)

