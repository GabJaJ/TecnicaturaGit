class Monitor: # clase independiente

    contador_monitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contador_monitores +=1
        self._id_moitor = Monitor.contador_monitores # conteo de la cantidad de monitores
        self._marca = marca   # encapsulamos los atributos
        self._tamaño = tamaño

    def __str__(self):
        return f'Id: {self._id_moitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'




# hacemos el test de comprobacion

if __name__ == '__main__':
    monitor1 = Monitor('Mac', '15')
    monitor2 = Monitor('Winco', '17')
    monitor3 = Monitor('HP', '19')
    print(monitor1,', ', monitor2)
    print(monitor3)
