class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, computadoras): # metodo agregar computadora donde se crea una  listado de computadoras
        self._computadoras.append(computadoras) # con el append se suma el objeto al listado

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() # se suma el str de la clase computadora
        return f'''
            Orden: {self._id_orden}
            Computadora: {computadoras_str}
        '''

