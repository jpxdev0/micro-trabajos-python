class Profesor:
    def __init__(self, nombre="Desconocido", apellido=None, Antiguedad=0):
        self.nombre = nombre
        self.apellido = apellido
        self.Antiguedad = Antiguedad

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Antiguedad: {self.Antiguedad} años"

lista = [
    Profesor("Adrian", "Vazquez", 16),
    Profesor("Irene", "Rodriguez", 28),
    Profesor("Daniel", "Olmos", 21)
]
n = input("Nombre del nuevo profesor> ")
a = input("Apellido del nuevo profesor> ")
t = int(input("Antiguedad del nuevo profesor> "))
lista.append(Profesor(n,a,t))

print("--------------------Lista de Profesores-------------------------:")
lista.sort(key=lambda year:year.Antiguedad)
print("Lista original:")
for x in lista:
    print(x)

print("------------------------------")
print("Lista ordenada por antiguedad:")
lista.sort(key=lambda year: year.Antiguedad)
for x in lista:
    print(x)

print("------------------------------")
print("Lista ordenada por apellido:")
lista.sort(key=lambda ape: ape.apellido)
for x in lista:
    print(x)

print("------------------------------")
print("Lista ordenada por nombre:")
lista.sort(key=lambda nom: nom.nombre)
for x in lista:    
    print(x)
#
# Ordenar los profesores por antiguedad
#nueva_lista = sorted(lista)
#print("Lista nueva")
#lista.sort()
#print("Lista ordenada por antiguedad:")
#for x in lista:
#    print(x)
#TODO: ordenar por varios elementos prioritarios...
#Primero antiguedad,Apellido,nombre
