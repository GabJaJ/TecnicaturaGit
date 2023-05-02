class Empleado:  # No hereda sino solo de la clase object
    def __init__(self, nombre, sueldo):
        self.nombre = nombre  # iniciamos los atributos
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):  # creamos un metodo
        return self.__str__()
