class Persona2:
    def __init__(self, nombre, apellido, edad): # los atributos con doble guion son encapsulados solo se pueden acceder a traves de GET o de SET tambien
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):  # METODO mostrar detalles
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')


    #def __init__(self, altura, sexo, profesion): # los atributos con doble guion son encapsulados solo se pueden acceder a traves de GET o de SET tambien
    #    self._altura = altura
    #    self._sexo = sexo
    #    self._profesion = profesion
    #def mostrar_detalles(self):  # METODO mostrar detalles
    #    print(f'Los datos agregador son: {self._altura} {self._sexo} {self._profesion}')


    #METODO GETTER
    @property #DECORADOR, nos permite acceder al metodo como si fuera un atributo y de manera indirecta.
    def nombre(self):
        print('Estamos utilizando el metodo GET en nombre')
        return self._nombre #retorna el metodo getter

    #METODO SETTER
    @nombre.setter
    def nombre(self, nombre):
        print('Estamos utilizando el metodo SET en nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        print('Estamos utilizando el metodo GET en apellido')
        return self._apellido


    @apellido.setter
    def apellido(self, apellido):
        print('Estamos utilizando el metodo SET en apellido')
        self._apellido = apellido

    @property
    def edad(self):
        print('Estamos utilizando el metodo GET en edad')
        return self._edad

    @edad.setter
    def edad(self, edad):
        print('Estamos utilizando el metodo SET en edad')
        self._edad = edad

    # METODO para BORRAR (DESTRUCTOR) se manda a llamar de manera automatica
    def __del__(self):
        print(f'Persona2 (desde metodo DESTRUCTOR): {self._nombre} {self._apellido} {self._edad}')


    #TAREA: crear tres objetos mas.


    #@altura.setter
    #def altua(self, altura):
    #    print('Estamos utilizando el metodo SET en altura')
    #    self._altura = altura

    #@property
    #def altura(self):
    #    print('Estamos utilizando el metodo GET en altura')
    #    return self._altura

    #@sexo.setter
    #def sexo(self, sexo):
    #    print('Estamos utilizando el metodo SET en sexo')
    #    self._sexo = sexo

    #@property
    #def sexo(self):
    #    print('Estamos utilizando el metodo GET en sexo')
    #    return self._sexo

    #@profesion.setter
    #def profesion(self, profesion):
    #    print('Estamos utilizando el metodo SET en altura')
    #    self._profesion = profesion

    #@property
    #def profesion(self):
    #    print('Estamos utilizando el metodo GET en altura')
    #    return self._profesion


if __name__ == '__main__': # impide que los datos del main se revelen al ejecutarse desde otro metodo importado

#Acceder a los atributos a traves del METODO GETTER Y SETTER

    print('Persona 1:')
    persona1 = Persona2('Gabriel', 'Juhasz', 37)
    #print(persona1._nombre)  esto ya no se debe hacer
    print(persona1.nombre) #estamos llamadno al metodo GETTER, que no necesita parametros,


    #TAREA: Agreggar el metodo GET y SET para los atributos apellido y edad

    print(persona1.apellido)
    print(persona1.edad)

    #Llamamos al METODO SET

    persona1.nombre = 'Juan Pedro' #Llamamos al METODO SETTER con el parametro el compilador ya sabe que necesitamos modificar
    print(persona1.nombre) #Otra vez el METODO GETTERnos muestra el metodo get pero utilizando el metodo set para modificarlo a traves de los metodos.
    print(persona1.mostrar_detalles()) #Llamamos al METODO mostrar_detalles, accedemos a los datos respetando el encapsulamiento

    #SETTER es para modificar lo que este dentro del ATRIBUTO
    #persona1.edad = 40 la variable edad se trasnsformaria en un READ ONLY porque no se puede modificar
    #persona1._edad = 40 ESTO NO ESTA BIEN! QEDARAS COMO UN IGNORANTE!!
    #print(persona1.edad) error: de Atributo, no se puede modificar el atributo EDAD, es por el encapulamiento

    print(persona1.edad) #mostra la edad a traves del METODO GET sin poder modificarse. SOLO LECTURA ya que no tiene el metodo set.

    # TAREA:
    print('Persona 2:')
    persona2 = Persona2('Javier', 'Petrowski', 26)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)

    persona2.nombre = 'Sebastian'
    persona2.apellido= 'Panello'
    persona2.edad = 29

    print(persona2.mostrar_detalles())

    print('Persona 3:')
    persona3 = Persona2('Agustin', 'Turen', 27)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)

    persona3.nombre = 'Sabrina'
    persona3.apellido= 'Oliguer'
    persona3.edad = 24

    print(persona3.mostrar_detalles())

    print('Persona 4:')
    persona4 = Persona2('Francisco', 'Regueiro', 32)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Daniel'
    persona4.apellido= 'Lingolli'
    persona4.edad = 34

    print(persona4.mostrar_detalles())

    #La diferencia del GETTER y SETTER
    #El metodo GETTER estamos utilizando el @property
    #EL SETTER aparte del SELF va a necesitar un parametro dentor del parentesis para modificar el valor dentro del ATRIBUTO


    print(__name__) # nos indica hasta donde queda el codigo de persona2