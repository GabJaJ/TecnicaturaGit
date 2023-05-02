class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamadas
    Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase
    padre debe tener los siguientes atributos y metodos:
    -Atributos(color, ruedas)
    -Metodos(__init__() y __str__())

    Auto(clase hija de Vehiculo)
    -Atributos(velocidad (km/hs))
    -Metodos(__init__() y __str__())

    Bicicleta(clase hija de Vehiculo)
    -Atributos(tipo(urbana/montaña/etc.))
    -Metodos(__init__(color, ruedas, tipo) y __str__())

    Crear un objeto de cada clase
    '''
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f'Vehiculo:  [Color: {self._color}, Ruedas: {self._ruedas} ]'

class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f'Auto: [ Velocidad(km/hs): {self._velocidad} ] {super().__str__()}' #c onstructor super de la clase object

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo


    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo:
        self._tipo = tipo


    def __str__(self):
        return f'Bicicleta: [ Tipo: {self._tipo} ] {super().__str__()}'




auto1 = Auto('Azul', 4, 190)
print(auto1.color)
print(auto1.ruedas)
print(auto1.velocidad)


bicicleta1 = Bicicleta('Rojo', 2, 'BMX')
print(bicicleta1.color)
print(bicicleta1.ruedas)
print(bicicleta1.tipo)


#Primer objeto de la clase padre Vehiculo
vehiculo= Vehiculo('blanco', 4)
print(vehiculo)

#Segundo objeto, pero ahora de la clase auto
auto = Auto('Amarillo', 4, 120)
print(auto)

#Tercer objeto, el ultimo de la clase Bicicleta
bici= bicicleta ('Azul', 2, 'Urbana')
print(bici)
