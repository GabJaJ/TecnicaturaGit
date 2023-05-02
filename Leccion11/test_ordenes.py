from Orden import Orden
from Producto import Producto

producto1 = Producto('Camiseta', 100.00)
print(producto1)
producto2 = Producto('Pantalon', 150.00)
print(producto2)
producto3 = Producto('Sweater', 180.00)  # agregamos productos
print(producto3)
producto4 = Producto('Anteojos', 120.00)
print(producto4)
producto5 = Producto('Medias', 80.00)
print(producto5)
producto6 = Producto('Guantes', 160.00)
print(producto6)

productos1 = [producto1, producto2]  # creamos una lista de productos

orden1 = Orden(productos1)  # agregamos la lista productos al primer objeto Orden
orden1.agregar_producto(producto5) # agregamos productos
orden1.agregar_producto(producto3)
print(orden1)
print(f'Total de la orden1: {orden1.calcular_total()}') # calculamos el total del precio de los producto

productos2 = [producto3, producto4]  # creamos una nueva lista

orden2 = Orden(productos2)  # modificamos la orden2 y agregamos nueva lista
orden2.agregar_producto(producto6)
orden2.agregar_producto(producto2)
print(orden2)
print(f'Total de la orden2: {orden2.calcular_total()}')

# probamos el metodo para agregar productos 5 y 6


