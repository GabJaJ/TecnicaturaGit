class MiClase: # la clase se carga en memoria
    #variable de clase, este atributo dará a cada objeto el mismo valor
    variable_clase = 'Esta es una variable de Clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


print(MiClase.variable_clase) # nos muestra el valor de la variable de Clase, accedemos directamente desde la misma clase

miClase1 = MiClase('Esta es una variable de Instancia') # creamos un objeto
print(miClase1.variable_instancia) # accedemos a traves del objeto.
print(miClase1.variable_clase)
miClase2 = MiClase('Esta es otra pruba de variable de Instancia')
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# los objetos tambien pueden acceder a la variable de clase

