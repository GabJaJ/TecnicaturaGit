from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

print('Creacion de objeto clase Cuadrado' .center(50, '_'))
cuadrado1 = Cuadrado(8, 'Azul')  #creamos un objeto de la clase cuadrado y le pasamos dos argumentos
cuadrado1.alto = 7  # modificamos los valores reasignando otro valor a traves de los metodos Getter, no hay control en la validacion, hya fallas, se creara un metodo encapsulado. en figura geometrica
cuadrado1.ancho = 7
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(f'Cálculo del área del Cuadrado: {cuadrado1.calcular_area()}') # llamamos al metodo



# MRO = Method Resolution Order, es importante saber le orden en el que se llaman la clases padres, se conoce la jerarquia de las clases padres.

print(Cuadrado.mro())

print(cuadrado1)
print('Creacion de objeto clase Rectangulo' .center(50, '_'))
rectangulo1 = Rectangulo(3, 9, 'amarillo')  #objeto rectangulo
rectangulo1.ancho = 8
print(f'Calculo del area del Rectangulo: {rectangulo1.calcular_area()}')
print(rectangulo1)

#creamos un objeto de la clase padre figuraGeometrica
#figura1 = FiguraGeometrica() # no se puede instanciar, es abstracta
print(Cuadrado.mro())
