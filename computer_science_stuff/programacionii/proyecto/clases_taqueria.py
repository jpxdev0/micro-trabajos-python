import random

class Instrumentos:
    def __init__(self):
        opciones_nombre = ['guitarra', 'tololoche', 'bajo', 'bateria']
        opciones_color = ['verde', 'rojo', 'blanco', 'morado']
        
        self.nombre = random.choice(opciones_nombre)
        self.color = random.choice(opciones_color)

    def __str__(self):
        return f"(soy una/un {self.nombre}, de color{self.color})"

mi_instrumento = Instrumentos()

