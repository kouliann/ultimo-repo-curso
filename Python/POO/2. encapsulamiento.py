class carro: 
    def __init__(self, marca, color, modelo):
        self._marca = marca
        self.__modelo = modelo
        self.color = color
        self.encendido = False
    
    #Getters y setters son metodos que nos permiten acceder (get) y modificar (set)
    def get_marca(self):
        print(self._marca)
        
    def set_marca(self, marca):
        self._marca = marca
        
    def encender(self):
        self.encendido = True
        print(f"El carro ha encendido ({self._marca}, {self.__modelo}).")
        
    def apagar(self):
        self.encendido: False
        print(f"El carro se ha apagado ({self._marca}, {self.__modelo}).")
        
    def acelerar(self):
        if self.encendido:
            print('el carro esta acelerando')
        else: 
            print('El carro debe estar encendido para acelerar')
            
mi_carro = carro("toyota", "corolla", "blanco")
mi_carro.set_marca("Nissan")
        
        