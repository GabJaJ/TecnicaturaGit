from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada): # la clase Raton hereda de la clase DispositivoEntrada

    contador_ratones = 0 # inicializamos el contador en 0

    def __init__(self, marca, tipo_entrada): # conteo de cada uno de los objetos de la clase raton
        Raton.contador_ratones += 1 # aumentamos en 1 el contador
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada) # llamamos a la herencia de la clase DispositivoEntrada con los argumentos de la clase

    def __str__(self):
        return f'Id: {self._id_raton}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'


# Hacemos pruebas

# creamos objetos de la clase raton
if __name__ == '__main__':
    raton1 = Raton('Genius', 'USB')
    raton2 = Raton('HP', 'USB-C')
    print(raton1,', ', raton2)
    raton3 = Raton('Acer', 'Bluetooth')
    print(raton3)
