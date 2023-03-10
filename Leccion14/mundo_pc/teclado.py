from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada): # conteo de cada uno de los objetos de la clase raton
        Teclado.contador_teclados += 1 # aumentamos en 1 el contador
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada) # llamamos a la herencia de la clase DispositivoEntrada con los argumentos de la clase

    def __str__(self):
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo Entrada: {self._tipo_entrada}'



if __name__ == '__main__':
    teclado1 = Teclado('Razer', 'USB')
    teclado2 = Teclado('Logitech', 'USB')
    teclado3 = Teclado('HP', 'Bluetooth')
    print(teclado1,', ', teclado2)
    print(teclado3)