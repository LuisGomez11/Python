class Empleado:

    def __init__(self,id,nombre,cargo,salario,email,telefono):
        self.id = id
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.email = email
        self.telefono = telefono

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getCargo(self):
        return self.cargo

    def getSalario(self):
        return self.salario

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def setId(self, nuevoId):
        self.id = nuevoId

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def setCargo(self, nuevoCargo):
        self.cargo = nuevoCargo

    def setSalario(self, nuevoSalario):
        self.salario = nuevoSalario

    def setEmail(self, nuevoEmail):
        self.email = nuevoEmail

    def setTelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
