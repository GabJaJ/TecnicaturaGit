from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self._productos = list(productos) # lista convertimos los productos a una lista y es lo que se asugna a su atrubuto productos

    def agregar_producto(self, producto): # este parametro recibe un objeto de producto
        self._productos.append(producto) # asi se agraga un nuevo producto al final de la lista

    def calcular_total(self): # metodo para calcular el total
        total = 0 # variable temporal para almacenar el calculo del total temporal
        for producto in self._productos: # recorremos los elementos de la list
            total += producto.precio # asignamos el valor parcial de cada producto con el setter
        return total

    def __str__(self): # convierte los productos en una cadena tipo string y habra que recorerla
        productos_str = '' # variable vacia
        for producto in self._productos: # reocorremos la lista de productos
            productos_str += producto.__str__()+' | ' # almacena los datos recibidos de la clase str prodictos, simbolo de pipe, separa cada uno de los productos
        return f'Orden: {self.id_orden}, \nProducto: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camiseta', 100.00)
    print(producto1)
    producto2 = Producto('Pantalon', 150.00)
    print(producto2)
    productos1 = [producto1, producto2]  # creamos una lista de productos
    orden1 = Orden(productos1) # agregamos la lista productos al primer objeto Orden
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)

# Tarea: Modificar la orden2 ingresando productos con sus nombres y precios
# crear una nueva lista de prodictos y agregarla a la orden2

    producto3 = Producto('Sweater', 180.00) # agregamos productos
    print(producto3)
    producto4 = Producto('Anteojos', 120.00)
    print(producto4)
    producto5 = Producto('Medias', 80.00)
    print(producto5)
    producto6 = Producto('Guantes', 160.00)
    print(producto6)
    productos2 = [producto3, producto4, producto5, producto6] # creamos una nueva lista
    orden2 = (productos2) # modificamos la orden2 y agregamos nueva lista
    print(orden2)
