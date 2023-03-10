from abc import ABC, abstractmethod #Abstract Base Class: convertimos la clase en abstracta, con su decorador Abstract Method


class FiguraGeometrica(ABC): # clase padre FiguraGeometrica, ahora es hija de la clase ABC abstracta
    def __init__(self, ancho, alto):
        if self._validar_valores(ancho): #0 < ancho < 10: #Sintaxis simplificada para preguntar un rango.
            self._ancho = ancho
        else:
            self.ancho = 0
            print(f'Valor erroneo para el ancho: {ancho}')
        if self._validar_valores(alto): #0 < alto < 10:    #Validacion
            self._alto = alto
        else:
            self._alto = 0
            print(f'Valor erroneo para el alto: {alto}') #se puede trabajar no solo con el metodo Dunder init sono que tambien en el metodo Setter

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho): # validacion correcta al metodo Set
            self._ancho = ancho
        else:
            print(f'Valor erroneo ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter  #quitando los metodos setter se establece el valor sin poder modificarlo
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo altura: {alto}')

    @abstractmethod # definimos al metodo abstracto
    def calcular_area(selfself):
        pass # de esta mandera se utiliza para definir un metodo ya definido en este caso sin implemetnacion ni error

    def __str__(self):
        return f'FiguraGeometrica [Ancho: {self._ancho}, Alto: {self._alto}]'


    def _validar_valores(self, valor): #metodo para encapsular de manera interna en la clase padre. se crea un parametro llamado valor
        return True if 0 < valor < 10 else False #
