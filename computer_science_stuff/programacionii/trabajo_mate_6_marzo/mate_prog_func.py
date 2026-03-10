import math

class Funciones:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def potencia(self, x):
        return self.b * (x ** (2 * self.a)) + self.c
        
    def exponencial(self, x):
        return self.b * math.exp(self.a * x)
        
    def logaritmica(self, x):
        if x <= 0 or self.a * x <= 0:
            return "Indefinido"
        return self.b * math.log(self.a * x)
        
    def trigonometrica(self, x):
        return self.b * math.sin(self.a * x)
        
    def radical(self, x):
        if self.a * x < 0:
            return "Indefinido"
        return self.b * math.sqrt(self.a * x) + self.c

    def funcion_master(self, x, termino):
        return termino(x)