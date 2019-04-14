
class Persona:

    nombre = ""
    direccion = ""

    def __init__(self,nombre,direccion):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, nuevaDire):
        self.direccion = nuevaDire

    def toString(self):
        print("Nombre:",self.nombre,"\nDireccion:",self.direccion)

class Estudiante(Persona):

    programa = ""
    anio = 0
    cuota = 0.0

    def __init__(self,nombre,direccion,programa,anio,cuota):
        self.nombre = nombre
        self.direccion = direccion
        self.programa = programa
        self.anio = anio
        self.cuota = cuota

    def getPrograma(self):
        return self.programa

    def getAnio(self):
        return self.anio

    def getCuota(self):
        return self.cuota

    def setPrograma(self, nuevoProgra):
        self.programa = nuevoProgra

    def setAnio(self, nuevoAnio):
        self.anio = nuevoAnio

    def setCuota(self, nuevaCuota):
        self.cuota = nuevaCuota

    def toString(self):
        print("\nNombre:",self.nombre,"\nDireccion:",self.direccion,
            "\nPrograma:",self.programa,"\nAño:",self.anio,"\nCuota:",
            self.cuota,"\n")

class Personal(Persona):

    colegio = ""
    paga = 0.0

    def __init__(self,nombre,direccion,colegio,paga):
        self.nombre = nombre
        self.direccion = direccion
        self.colegio = colegio
        self.paga = paga

    def getColegio(self):
        return self.colegio

    def getPaga(self):
        return self.paga

    def setColegio(self, nuevoCole):
        self.colegio = nuevoCole

    def setPaga(self, nuevaPaga):
        self.paga = nuevaPaga

    def toString(self):
        print("\nNombre:",self.nombre,"\nDireccion:",self.direccion,
            "\nColegio:",self.colegio,"\nPaga:",self.paga,"\n")


estu = Estudiante("Luis","San Francisco","TDS",2016,2.5)

perso = Personal("Diana","Santa Maria","Tecno Comfenalco",250.5)

estu.toString()
perso.toString()