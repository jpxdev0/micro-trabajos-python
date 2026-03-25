class Empleado:
    #Nombre, id, sueldo, antiguedad
    def __init__(self,ID,nombre, antiguedad, sueldo):
        self.nombre = nombre
        self.ID = ID
        self.antiguedad = antiguedad
        self.sueldo = -1
    def __str__(self):
        return f"El empleado {self.nombre}, de Id{self.ID}, de antiguedad{self.antiguedad},con sueldo de {self.sueldo}"
        
    