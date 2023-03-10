class Persona: # Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre #inicializamos sus atributos
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad


    def __str__(self): # Override = sobreescribir, este metodo sobreescribe los atributos, lo que recibe y al ser miembro de la misma clase tiene acceso. tipo String.
        return f'Persona:  [Nombre: {self._nombre}, Edad: {self._edad} ]'


class Empleado(Persona): #la calse Empleado es hija de la clase Persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) # hacemos uso de las caracteristicas del padre Persona
        self._sueldo = sueldo



    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self): # Metodo DUnder STR (double under)
        return f'Empleado: [ Sueldo: {self._sueldo} ] {super().__str__()}' #sobreescribimos el str de la clase hija llamando al str de la clase padre sobreescribiendola




empleado1 = Empleado('Gabriel', 37, 75000) #Creamos un objeto.
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea crear el encapsulamiento y agregar los metodos Getter and Setter

empleado2 = Empleado('Agustiina', 25, 85000)
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)

empleado2.nombre = 'Marta'
empleado2.edad = 39
empleado2.sueldo= 79000
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)



