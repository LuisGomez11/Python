class Vehiculo:
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def getMarca(self):
        return self.marca

    def getModelo(self):
        return self.modelo

    def getColor(self):
        return self.color

    def setMarca(self, nuevoMarca):
        self.marca = nuevoMarca

    def setModelo(self, nuevoModelo):
        self.modelo = nuevoModelo

    def setColor(self, nuevoColor):
        self.color = nuevoColor
