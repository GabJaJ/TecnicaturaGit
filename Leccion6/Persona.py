class Persona:  # Creamos una clase (Plantilla)
    # pass   # No se procesa nada mas (No tiene contenido)
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):  # Se lo llama METODO Init: double underscore 'Dunder'
        self.nombre = nombre  #ATRIBUTOS ENCAPSULADOS, manejados de forma PUBLICA, doble guion bajo evita que sea modificado
        self.apellido = apellido #en python no hay modificadores de acceso, son de tipo public, para hacerlo privado se le agrega un guion bajo
        self._dni = dni    # este ATRIBUTO esta ENCAPSULADO de una manera sugerida (PRIVADA)
        self.edad = edad
        self.args = args #permite pasar argumetos variables de tipo diccionario, Tupla, etc.
        self.wkargs = kwargs #permite pasar argumetos variables de tipo diccionario,

        # self.nombre = 'Juan' #Atributos dentro de un metodo
        # self.apellido = 'Zalazar'
        # self.edad = 22

    def mostrar_detalle(self):  # metodo de instancia, "self" en java se conoce como "this"
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son:  {self.wkargs}')


persona1 = Persona('Gabriel', 'Juhasz', 31777222, 37)  # necesitamos enviar argumentos

print(type(Persona))
#print(Persona)  # tarea: hacer el print igual que con el objeto 2
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}')

persona2 = Persona('Ariel', 'Betancud', 32456987, 40)  # Necesitamos enviar argumentos
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} su edad es {persona2.edad}')

print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} su edad es {persona1.edad}')

# Los objetos no comparten valores solo los atributos y asi podemos asignar diferentes valores a cada atributo
# Atributos de instancia de objetos se asginan a los objetos yu no comparten informacion.

# MODIFICAMOS los ATRIBUTOS de persona1 al ser PUBLICOS desde sus instancias (objetos)
persona1.nombre = 'Osvaldo'
persona1.apellido = 'Giordanini'
persona1.edad = 45
print(f'El objeto modificado de la calse persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}')

# Objetos de Instancia UML

# Los atributos son: caracteristicas para nuestros objetos
# Los metodos son: el comportamiento que van a tener los objetos (acciones) un metodo es igual a una funcion
# El metodo esta asociada a una clase y la funcion es propia de si misma

persona1.mostrar_detalle()  # llamamos al metodo desde un objeto transformado en  variable a traves del operador de punto podemos acceder a los metodos y atributos
persona2.mostrar_detalle()  # la referencia se pasa de manera automatica, no se utilisa el self que solo va dentro de un metodo

# Persona.mostrar_detalle(persona1) #No es eficaz, aca utilizamos la clase para llamar un metodo y si o si hay que pasar una referencia

persona1.telefono = '44552332'  # se crea un atributo superficial solo para este objeto. persona2 no puedwe dar uso de este atributo
print(f'Este es el telefono de: {persona1.nombre} {persona1.telefono}')  # hemos creado un atributo de un objeto

# print(persona2.telefono)  # el objeto persona2 no tiene este atributo, da error

persona3 = Persona('Rogelio', 'Romero', 32567324, 22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18,
                   Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()

# print(persona3._dni)  # esto NO debe utilizarse, python interpreta esto como sugerencia y va a acceder igual al dato, dice que desconocemos python.


#doble guion bajon en el atributo __ ENCAPSULAMIENTO ESTRICTO

#persona3.__nombre # error en la clase persona el objeto el objeto no tiene atributo, esta completamente encapsulado

