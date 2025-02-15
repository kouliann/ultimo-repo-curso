#polimorfismo

#es la capacidad de un objeto de comportarse de diferentes formas
#va a tener diferente comportamiento dependiendo de la situacion

class Restaurante: 
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categotria = categoria
        self.precio = precio
        
    def agregarRestaurante(self, nombre):
        self.nombre = nombre
        print(f"agregar restaurante...{self.nombre}")
        
    def mostrarRestaurante(self):
        print(f'el nombre del restaurante es: {self.nombre} y es de la categoria: {self.categotria}')
        
    
restaurantes= Restaurante("el caballo sediento", "Bar", 50)
restaurantes.mostrarRestaurante()


#herencia

class Hotel(Restaurante):
    def  __init__(self, nombre, categoria, precio, numero_habitaciones, piscina):
        super().__init__(nombre, categoria, precio)
        self.numero_habitaciones = 40
        self.piscina = False
    
    def get_piscina(self):
        return self.piscina
    
    #Reescribir el metodo mostrar_informacion y debe llamarse igual
    def mostrarRestaurante(self):
        super().mostrarRestaurante()
        print(f"numero de habitaciones: {self.numero_habitaciones}")
        print(f"Tiene piscina {'Si' if self.piscina else 'no'}")
        
restaurantes= Restaurante("el caballo sediento", "Bar", 50)
restaurantes.mostrarRestaurante()

hotel = Hotel("Hotel POO", "5 estrellas", 500, 100, True)
hotel.mostrarRestaurante()