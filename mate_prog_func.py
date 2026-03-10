import random
import math


class Funciones:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def potencia(self, x):
        return self.a * x**self.b

    def exponencial(self, x):
        return self.a * math.exp(self.b * x)

    def logaritmica(self, x):
        return self.a * math.log(x)

    def trigonometrica(self, x):
        return self.a * math.sin(self.b * x)

    def logaritmo(self, x):
        return self.a * math.log(x)

    def radical(self, x):
        return self.a * math.sqrt(x)

    def funcion(self, x, termino):
        if termino == "potencia":
            return self.potencia(x)
        elif termino == "exponencial":
            return self.exponencial(x)
        elif termino == "logaritmica":
            return self.logaritmica(x)
        elif termino == "trigonometrica":
            return self.trigonometrica(x)
        elif termino == "logaritmo":
            return self.logaritmo(x)
        elif termino == "radical":
            return self.radical(x)
        else:
            return "Termino no valido"

    def integral(self, termino):
        if termino == "potencia":
            return self.a * x ** (self.b + 1) / (self.b + 1)
        elif termino == "exponencial":
            return self.a * math.exp(self.b * x) / self.b
        elif termino == "logaritmica":
            return self.a * (x * math.log(x) - x)
        elif termino == "trigonometrica":
            return self.a * -math.cos(self.b * x) / self.b
        elif termino == "logaritmo":
            return self.a * (x * math.log(x) - x)
        elif termino == "radical":
            return self.a * 2 * x ** (self.b + 1) / (self.b + 1)
        else:
            return "Termino no valido"

    def __str__(self):
        return f"a = {self.a}, b = {self.b}, c = {self.c}"

    def crea_funciones(cls):
        a = random.randint(1, 10)
        b = random.uniform(1, 10)
        c = random.uniform(-10, 10)
        return Funciones(a, b, c)

    def __lt__(self, other):
        return self.a < other.a

    def __gt__(self, other):
        return self.a > other.a
