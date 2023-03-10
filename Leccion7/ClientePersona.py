from Persona import *  #importamos todas las clases que hubiesen mas su modulo

persona1 = Persona ('Carlos', 42) # Creamos un objeto persona en la clase Persona
print(persona1) #nos muestra el espacio de memoria


#accedemos a los atributos de la clase Empleado (hija)
#creamos un objeto de lo que es la clase empleado

empleado3 = Empleado('Jorge', 45, 80000)
print(empleado3) #acude al metodo dunder str sobreescrito de la clase padre object, heredando las caracteristicas de esa clase
