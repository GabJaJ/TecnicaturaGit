class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre # inicializamos los atributos
        self.edad = edad

    #sobreescribimos un metodo en este caso de suma

    def __add__(self, other): # el parametro other se puede cambair por cualqueir otro es solo de referencia hacia otro
        return f'{self.nombre} {other.nombre}'  # el metodo necesita un retorno
      # return f'self.nombre + other.nombre'

    def __sub__(self, otro): # metodo de resta
        return self.edad - otro.edad

persona1 = Persona('Javier', 34) # creamos un objeto
persona2 = Persona('Luchetti', 22)

# persona1.__add__(persona2) # sintaxis interna y automatica que sucede al exponer un obketo con el otro pero no es acostumbrado

print(persona1 + persona2) # une solo los nombres tipo string
print(persona1 - persona2) # va a restar los valores numericos


