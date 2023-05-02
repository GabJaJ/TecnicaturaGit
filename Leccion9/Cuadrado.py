from Color import Color # from (modulo/archivo) import (clase)
from FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica, Color): # clase hija de FiguraGeometrica y Color. / herencia multiple.
    def __init__(self, lado, color):#inicializamos la clase hija de forma correcta con el metodo DUnder init
        # super.__init__(lado) / utilizamos el constructor super para llamar a la clase padre ne la clase hija pero no se utiliza para evitar confuciones , no se utiliza en hernecia multiple
        FiguraGeometrica.__init__(self, lado, lado)# llamamos directamente a la clase padre
        Color.__init__(self, color)# indicamos un lado de ancho y otro lado de alto

    def calcular_area(self): #metodo para multiplicar el lado alto por el lado ancho
        return  self.alto * self.ancho

    def __str__(self):
        return f' {FiguraGeometrica.__str__(self)}{Color.__str__(self)}'



