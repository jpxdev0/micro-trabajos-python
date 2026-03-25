import math

class Funciones:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def potencia(self, x):
        return self.b * (x ** (2 * self.a)) + self.c
        
    def exponencial(self, x):
        try:
            return self.b * math.exp(self.a * x)
        except OverflowError:
            return "Indefinido (Overflow)"
        
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

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Figuras:
    def __init__(self, p1, p2, p3, p4):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def calcular_pendiente(self, punto_inicio, punto_fin):
        x1 = punto_inicio.x
        y1 = punto_inicio.y
        x2 = punto_fin.x
        y2 = punto_fin.y
        
        if x2 - x1 == 0:
            return "vertical"
            
        m = (y2 - y1) / (x2 - x1)
        return round(m, 4)

    def clasificar_figura(self):
        m1 = self.calcular_pendiente(self.p1, self.p2) 
        m2 = self.calcular_pendiente(self.p2, self.p3) 
        m3 = self.calcular_pendiente(self.p3, self.p4) 
        m4 = self.calcular_pendiente(self.p4, self.p1) 
        
        paralelos_arriba_abajo = (m1 == m3)
        paralelos_izq_der = (m2 == m4)
        
        if paralelos_arriba_abajo and paralelos_izq_der:
            return "paralelogramo"
        elif paralelos_arriba_abajo or paralelos_izq_der:
            return "trapecio"
        else:
            return "cuadrilatero comun"