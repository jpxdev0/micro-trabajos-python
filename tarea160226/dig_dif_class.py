import random
def dar_bienvenida(nombre):
    nombre = input("Ingrese su nombre: ")
    print(f"Bienvenido {nombre} al juego de dígitos diferentes!")
def pedir_numero():
    while True:
        numero = input("Ingrese un numero entre el valor del 1 al 10 para que esta sea su longitud: ")
        try:
            numero = int(numero)
            if numero < 2 or numero > 10:
                print("Error, necesitas poner un numero entre 2 y 10")
            else:
                return numero
        except ValueError:
            print("Error, ingresa un numero valido")
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.longitud = 0
    def pedir_longitud(self):
        self.longitud = pedir_numero()
        return self.longitud
# 4. Clase NumeroRaro
class NumeroRaro:
    def __init__(self, longitud):
        self.longitud = longitud
        self.digitos = []
    
    def validar_digito(self, nuevo_digito):
        # Verifica que el digito no este repetido
        return nuevo_digito not in self.digitos
    
    def generar_valor(self):
        # Generar el primer digito (no puede ser 0)
        primer_digito = random.randint(1, 9)
        self.digitos.append(primer_digito)
        
        # Generar el resto de digitos
        while len(self.digitos) < self.longitud:
            nuevo_digito = random.randint(0, 9)
            if self.validar_digito(nuevo_digito):
                self.digitos.append(nuevo_digito)
        
        # Convertir la lista de digitos a un numero
        numero_final = int(''.join(map(str, self.digitos)))
        return numero_final