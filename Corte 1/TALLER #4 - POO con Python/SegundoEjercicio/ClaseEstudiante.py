class Estudiante:

    def __init__(self,id,nombre,programa,semestre,institucion,email,telefono):
        self.id = id
        self.nombre = nombre
        self.programa = programa
        self.semestre = semestre
        self.institucion = institucion
        self.email = email
        self.telefono = telefono

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getPrograma(self):
        return self.programa

    def getSemestre(self):
        return self.semestre

    def getInstitucion(self):
        return self.institucion

    def getEmail(self):
        return self.email

    def getTelefono(self):
        return self.telefono

    def setId(self, nuevoId):
        self.id = nuevoId

    def setNombre(self, nuevoNombre):
        self.nombre = nuevoNombre

    def setPrograma(self, nuevoPrograma):
        self.programa = nuevoPrograma

    def setSemestre(self, nuevoSemestre):
        self.semestre = nuevoSemestre

    def setInstitucion(self, nuevaInstitucion):
        self.institucion = nuevaInstitucion

    def setEmail(self, nuevoEmail):
        self.email = nuevoEmail

    def setTelefono(self, nuevoTelefono):
        self.telefono = nuevoTelefono
