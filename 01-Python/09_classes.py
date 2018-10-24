class Auto:
    __ensamblado = 'Quito'
    numero_asientos = 5


    def __init__(self,nombre, color):
        self.nombre = nombre
        self.color = color

    def cambiar_ensamblado(self,ensamblado):
        self.__ensamblado = ensamblado

    def __maximo_numero_pasajeros(self):
        return self.numero_asientos + 3

    def __str__(self):
        print(self.nombre)
        print(self.color)
        print(self.__ensamblado)
        print(self.numero_asientos)
        print(self.__maximo_numero_pasajeros())


class Hyundai(Auto):
    def __init__(self,color,nombre):
        super().__init__(color=color,nombre=nombre)
        print('construcor')
        print(self.__ensamblado)


class Escuela:

    __ciudad = 'Quito'  # atributo privado
    pais = 'Ecuador'    # atributo publico


    def __init__(self,nombre,valor_categoria):
        print(self)
        print("Hola constructor")
        self.nombre = nombre
        self.valor_categoria = valor_categoria

    def saludar(self):
        print(f'Hola desde {self.nombre}'
              f' localizada en {self.__ciudad}')

    def categoria(self):
        return self.__calular_categoria()

    #Metodo privado
    def __calular_categoria(self):
        return self.valor_categoria*3

    # Metodo toString
    def __str__(self):
        return 'Escuela'




twa = Escuela(nombre='FESVIP',valor_categoria=4)
twa.saludar()


bm = Auto(color='Blanco',nombre='V 3')
print(bm)

bm.cambiar_ensamblado('Guayaquil')
print(bm)
